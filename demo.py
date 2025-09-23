#!/usr/bin/env python3
"""
Demo script showcasing ASCII Art Converter capabilities
"""

import os
from PIL import Image, ImageDraw, ImageFont
from ascii_art_converter import ASCIIArtConverter


def create_demo_images():
    """Create various demo images to showcase different conversion styles"""
    
    # Demo 1: Simple geometric pattern
    print("Creating geometric pattern demo...")
    img = Image.new('RGB', (300, 200), 'white')
    draw = ImageDraw.Draw(img)
    
    # Draw concentric circles
    for i in range(5):
        radius = 20 + i * 15
        x1, y1 = 150 - radius, 100 - radius
        x2, y2 = 150 + radius, 100 + radius
        color = int(50 + i * 40)
        draw.ellipse([x1, y1, x2, y2], outline=(color, color, color), width=3)
    
    img.save('demo_geometric.png')
    
    # Demo 2: Text image
    print("Creating text demo...")
    img = Image.new('RGB', (400, 150), 'white')
    draw = ImageDraw.Draw(img)
    
    try:
        # Try to use a better font if available
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 40)
    except:
        font = ImageFont.load_default()
    
    draw.text((50, 50), 'ASCII ART', fill='black', font=font)
    img.save('demo_text.png')
    
    # Demo 3: Gradient
    print("Creating gradient demo...")
    img = Image.new('RGB', (300, 200), 'white')
    for x in range(300):
        for y in range(200):
            intensity = int(255 * x / 300)
            img.putpixel((x, y), (intensity, intensity, intensity))
    
    img.save('demo_gradient.png')
    
    return ['demo_geometric.png', 'demo_text.png', 'demo_gradient.png']


def demonstrate_conversions():
    """Demonstrate different conversion options"""
    
    print("=== ASCII Art Converter Demo ===\n")
    
    # Create demo images
    demo_files = create_demo_images()
    
    # Test different character sets and widths
    char_sets = ['detailed', 'simple', 'blocks']
    widths = [40, 60, 80]
    
    for demo_file in demo_files:
        print(f"\n--- Processing {demo_file} ---")
        
        for char_set in char_sets:
            print(f"\n{char_set.upper()} CHARACTER SET:")
            print("-" * 50)
            
            converter = ASCIIArtConverter(char_set=char_set)
            try:
                ascii_art = converter.convert_image_to_ascii(demo_file, width=60)
                # Show first 10 lines
                lines = ascii_art.split('\n')[:10]
                for line in lines:
                    print(line)
                if len(ascii_art.split('\n')) > 10:
                    print("... (truncated)")
                
                # Save full version
                output_file = f"{demo_file[:-4]}_{char_set}.txt"
                converter.save_ascii_art(ascii_art, output_file)
                print(f"Full version saved to: {output_file}")
                
            except Exception as e:
                print(f"Error processing {demo_file} with {char_set}: {e}")
    
    # Cleanup demo images
    print("\nCleaning up demo images...")
    for demo_file in demo_files:
        if os.path.exists(demo_file):
            os.remove(demo_file)
    
    print("\nDemo completed! Check the generated .txt files for full ASCII art.")
    print("\nTo run the web interface, use: python web_interface.py")
    print("To convert your own images, use: python ascii_art_converter.py your_image.jpg")


if __name__ == "__main__":
    demonstrate_conversions()