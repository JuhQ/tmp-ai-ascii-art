#!/usr/bin/env python3
"""
Web interface for ASCII Art Converter using Flask
"""

from flask import Flask, request, render_template_string, jsonify, send_file
from ascii_art_converter import ASCIIArtConverter
import os
import tempfile
from werkzeug.utils import secure_filename
import base64
from io import BytesIO

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ASCII Art Converter</title>
    <style>
        body {
            font-family: 'Courier New', monospace;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #1a1a1a;
            color: #00ff00;
        }
        .container {
            background-color: #000;
            border: 2px solid #00ff00;
            border-radius: 10px;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #00ff00;
            text-shadow: 0 0 10px #00ff00;
        }
        .upload-section {
            margin: 20px 0;
            padding: 20px;
            border: 1px solid #333;
            border-radius: 5px;
        }
        .controls {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        label {
            display: block;
            margin-bottom: 5px;
            color: #00ff00;
        }
        input, select {
            width: 100%;
            padding: 8px;
            background-color: #333;
            color: #00ff00;
            border: 1px solid #00ff00;
            border-radius: 3px;
        }
        button {
            background-color: #000;
            color: #00ff00;
            border: 2px solid #00ff00;
            padding: 10px 20px;
            cursor: pointer;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            transition: all 0.3s;
        }
        button:hover {
            background-color: #00ff00;
            color: #000;
            box-shadow: 0 0 10px #00ff00;
        }
        .ascii-output {
            background-color: #000;
            color: #00ff00;
            padding: 20px;
            border: 1px solid #333;
            border-radius: 5px;
            white-space: pre;
            font-family: 'Courier New', monospace;
            font-size: 8px;
            line-height: 1;
            overflow-x: auto;
            max-height: 500px;
            overflow-y: auto;
        }
        .loading {
            text-align: center;
            color: #ffff00;
        }
        .error {
            color: #ff0000;
            border-color: #ff0000;
        }
        .file-info {
            margin: 10px 0;
            color: #888;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎨 ASCII Art Converter 🎨</h1>
        <p style="text-align: center;">Transform images into beautiful ASCII art using AI-powered image processing</p>
        
        <div class="upload-section">
            <h3>Upload Image</h3>
            <form id="uploadForm" enctype="multipart/form-data">
                <input type="file" id="imageFile" name="file" accept="image/*" required>
                <div class="file-info" id="fileInfo"></div>
                
                <div class="controls">
                    <div>
                        <label for="width">Width (characters):</label>
                        <input type="number" id="width" name="width" value="100" min="20" max="200">
                    </div>
                    <div>
                        <label for="charSet">Character Set:</label>
                        <select id="charSet" name="char_set">
                            <option value="detailed">Detailed ( .:-=+*#%@ )</option>
                            <option value="simple">Simple ( .:-# )</option>
                            <option value="blocks">Blocks ( ░▒▓█ )</option>
                        </select>
                    </div>
                    <div>
                        <label for="contrast">Contrast:</label>
                        <input type="number" id="contrast" name="contrast" value="1.5" min="0.5" max="3.0" step="0.1">
                    </div>
                </div>
                
                <button type="submit">Convert to ASCII Art</button>
            </form>
        </div>
        
        <div id="result" style="display: none;">
            <h3>ASCII Art Result</h3>
            <button onclick="downloadASCII()">Download as Text File</button>
            <div id="asciiOutput" class="ascii-output"></div>
        </div>
        
        <div id="loading" class="loading" style="display: none;">
            <h3>Converting image to ASCII art...</h3>
            <p>This may take a moment depending on image size and settings.</p>
        </div>
    </div>

    <script>
        let currentASCII = '';
        
        document.getElementById('imageFile').addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const fileInfo = document.getElementById('fileInfo');
                fileInfo.innerHTML = `Selected: ${file.name} (${(file.size / 1024 / 1024).toFixed(2)} MB)`;
            }
        });
        
        document.getElementById('uploadForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData();
            const fileInput = document.getElementById('imageFile');
            const file = fileInput.files[0];
            
            if (!file) {
                alert('Please select an image file');
                return;
            }
            
            formData.append('file', file);
            formData.append('width', document.getElementById('width').value);
            formData.append('char_set', document.getElementById('charSet').value);
            formData.append('contrast', document.getElementById('contrast').value);
            
            document.getElementById('loading').style.display = 'block';
            document.getElementById('result').style.display = 'none';
            
            try {
                const response = await fetch('/convert', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                
                if (data.success) {
                    currentASCII = data.ascii_art;
                    document.getElementById('asciiOutput').textContent = data.ascii_art;
                    document.getElementById('result').style.display = 'block';
                } else {
                    alert('Error: ' + data.error);
                }
            } catch (error) {
                alert('Error converting image: ' + error.message);
            } finally {
                document.getElementById('loading').style.display = 'none';
            }
        });
        
        function downloadASCII() {
            if (!currentASCII) return;
            
            const blob = new Blob([currentASCII], { type: 'text/plain' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'ascii_art.txt';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/convert', methods=['POST'])
def convert_image():
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file uploaded'})
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'})
        
        if not allowed_file(file.filename):
            return jsonify({'success': False, 'error': 'Invalid file type'})
        
        # Get parameters
        width = int(request.form.get('width', 100))
        char_set = request.form.get('char_set', 'detailed')
        contrast = float(request.form.get('contrast', 1.5))
        
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
            file.save(tmp_file.name)
            
            # Convert to ASCII
            converter = ASCIIArtConverter(char_set=char_set)
            ascii_art = converter.convert_image_to_ascii(
                tmp_file.name, 
                width=width, 
                contrast=contrast
            )
            
            # Clean up temp file
            os.unlink(tmp_file.name)
            
            return jsonify({
                'success': True, 
                'ascii_art': ascii_art,
                'width': width,
                'char_set': char_set
            })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    print("Starting ASCII Art Converter Web Server...")
    print("Visit http://localhost:5000 to use the web interface")
    app.run(debug=True, host='0.0.0.0', port=5000)