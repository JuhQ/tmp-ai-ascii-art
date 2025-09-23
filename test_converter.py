#!/usr/bin/env python3
"""
Test script for ASCII Art Converter
"""

import os
import sys
from PIL import Image, ImageDraw
from ascii_art_converter import ASCIIArtConverter


def create_test_image(filename="test_image.png", size=(200, 150)):
    """Create a simple test image for testing"""
    # Create a new image with gradient and shapes
    image = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(image)
    
    # Draw gradient background
    for y in range(size[1]):
        intensity = int(255 * y / size[1])
        color = (intensity, intensity, intensity)
        draw.line([(0, y), (size[0], y)], fill=color)
    
    # Draw some shapes
    draw.ellipse([50, 30, 150, 120], fill="black")
    draw.rectangle([10, 10, 40, 40], fill="white")
    draw.polygon([(160, 20), (190, 20), (175, 50)], fill="gray")
    
    image.save(filename)
    return filename


def test_ascii_converter():
    """Test the ASCII art converter with different settings"""
    print("Testing ASCII Art Converter...")
    
    # Create test image
    test_image_path = create_test_image()
    print(f"Created test image: {test_image_path}")
    
    # Test different character sets
    char_sets = ["detailed", "simple", "blocks"]
    
    for char_set in char_sets:
        print(f"\n--- Testing with '{char_set}' character set ---")
        converter = ASCIIArtConverter(char_set=char_set)
        
        try:
            ascii_art = converter.convert_image_to_ascii(test_image_path, width=60)
            print(ascii_art[:300] + "..." if len(ascii_art) > 300 else ascii_art)
            
            # Save to file
            output_file = f"test_output_{char_set}.txt"
            converter.save_ascii_art(ascii_art, output_file)
            print(f"Saved ASCII art to: {output_file}")
            
        except Exception as e:
            print(f"Error testing {char_set}: {e}")
    
    # Clean up test image
    if os.path.exists(test_image_path):
        os.remove(test_image_path)
    
    print("\nTest completed!")


if __name__ == "__main__":
    test_ascii_converter()