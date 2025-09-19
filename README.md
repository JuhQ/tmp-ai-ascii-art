# 🎨 AI ASCII Art Converter

Transform any image into beautiful ASCII art using intelligent image processing algorithms. This tool uses AI-like techniques to analyze images and convert them into text-based art with multiple character sets and customization options.

![ASCII Art Example](https://img.shields.io/badge/ASCII-Art-brightgreen) ![Python](https://img.shields.io/badge/Python-3.7%2B-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- **Multiple Character Sets**: Choose from detailed, simple, or block characters
- **Intelligent Processing**: AI-powered image analysis with contrast enhancement
- **Web Interface**: Easy-to-use web UI for drag-and-drop conversion
- **Command Line Interface**: Full CLI support for batch processing
- **Customizable Output**: Adjust width, contrast, and character density
- **Multiple Formats**: Support for JPEG, PNG, GIF, BMP, and TIFF images
- **Export Options**: Save ASCII art to text files

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/JuhQ/tmp-ai-ascii-art.git
cd tmp-ai-ascii-art

# Install dependencies
pip install -r requirements.txt
```

### Command Line Usage

```bash
# Basic conversion
python ascii_art_converter.py image.jpg

# Custom width and output file
python ascii_art_converter.py image.png --width 80 --output art.txt

# Different character sets
python ascii_art_converter.py photo.jpg --chars blocks --contrast 2.0

# See all options
python ascii_art_converter.py --help
```

### Web Interface

```bash
# Start the web server
python web_interface.py

# Open browser to http://localhost:5000
```

## 📖 Usage Examples

### Character Set Comparison

The tool offers three character sets for different aesthetic preferences:

**Detailed** (default): ` .:-=+*#%@`
- Best for high-detail images
- 10 character gradients
- Smooth transitions

**Simple**: ` .:-#`
- Clean, minimalist look
- 4 character gradients
- Good for logos and simple images

**Blocks**: ` ░▒▓█`
- Modern block appearance
- Unicode block characters
- Great for artistic effects

### Command Line Examples

```bash
# Portrait with detailed characters
python ascii_art_converter.py portrait.jpg --width 60 --chars detailed

# Landscape with blocks
python ascii_art_converter.py landscape.png --width 120 --chars blocks --output landscape_art.txt

# High contrast conversion
python ascii_art_converter.py photo.jpg --contrast 2.5 --width 100
```

## 🛠️ Technical Details

### Image Processing Pipeline

1. **Image Loading**: Support for multiple formats using PIL
2. **Resizing**: Intelligent aspect ratio preservation
3. **Grayscale Conversion**: Optimized luminance calculation
4. **Contrast Enhancement**: Adaptive contrast adjustment
5. **Character Mapping**: Pixel intensity to ASCII character conversion
6. **Output Formatting**: Line-based text formatting

### AI-Like Features

- **Adaptive Aspect Ratio**: Automatically adjusts for character height/width ratio
- **Contrast Enhancement**: Intelligent contrast boosting for better ASCII representation
- **Pixel Density Analysis**: Smart character mapping based on visual density
- **Edge Preservation**: Maintains important image details in ASCII conversion

## 🎯 Use Cases

- **Digital Art**: Create unique text-based artwork
- **Terminal Graphics**: Display images in text-only environments
- **Retro Computing**: Generate ASCII art for vintage systems
- **Social Media**: Create interesting text-based posts
- **Documentation**: Add visual elements to plain text documents
- **Programming**: Generate ASCII banners and headers

## 📊 Performance

- **Speed**: Processes most images in under 2 seconds
- **Memory**: Optimized for low memory usage
- **Scalability**: Handles images up to 16MB via web interface
- **Quality**: Maintains visual fidelity through intelligent processing

## 🔧 Configuration Options

### CLI Parameters

| Parameter | Description | Default | Range |
|-----------|-------------|---------|-------|
| `--width` | Output width in characters | 100 | 20-200 |
| `--chars` | Character set (detailed/simple/blocks) | detailed | - |
| `--contrast` | Contrast enhancement factor | 1.5 | 0.5-3.0 |
| `--output` | Output file path | stdout | - |

### Web Interface Settings

- **Upload**: Drag & drop or file selection
- **Real-time Preview**: Instant parameter adjustment
- **Download**: One-click text file export
- **Responsive**: Works on desktop and mobile

## 🐛 Troubleshooting

### Common Issues

**File Not Found**
```bash
Error: Image file 'image.jpg' not found
```
*Solution*: Check file path and ensure image exists

**Memory Error**
```bash
Error processing image: cannot identify image file
```
*Solution*: Ensure file is a valid image format

**Large File Upload**
```bash
413 Request Entity Too Large
```
*Solution*: Resize image or use CLI for large files

## 🤝 Contributing

We welcome contributions! Please feel free to submit pull requests, report bugs, or suggest features.

### Development Setup

```bash
# Clone and setup
git clone https://github.com/JuhQ/tmp-ai-ascii-art.git
cd tmp-ai-ascii-art
pip install -r requirements.txt

# Run tests
python test_converter.py

# Start development server
python web_interface.py
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🌟 Acknowledgments

- Built with Python and PIL (Pillow)
- Inspired by classic ASCII art techniques
- Modern web interface using Flask
- AI-enhanced image processing algorithms

---

**Made with ❤️ for the ASCII art community**