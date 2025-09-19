#!/usr/bin/env python3
"""
ASCII Art Converter - Convert images to ASCII art using AI-like image processing
"""

import argparse
import sys
from PIL import Image, ImageEnhance
import os


class ASCIIArtConverter:
    """Convert images to ASCII art using intelligent character mapping"""
    
    # Character sets ordered by visual density (light to dark)
    ASCII_CHARS_DETAILED = " .:-=+*#%@"
    ASCII_CHARS_SIMPLE = " .:-#"
    ASCII_CHARS_BLOCKS = " ░▒▓█"
    
    def __init__(self, char_set="detailed"):
        """Initialize converter with specified character set"""
        if char_set == "simple":
            self.ascii_chars = self.ASCII_CHARS_SIMPLE
        elif char_set == "blocks":
            self.ascii_chars = self.ASCII_CHARS_BLOCKS
        else:
            self.ascii_chars = self.ASCII_CHARS_DETAILED
    
    def resize_image(self, image, new_width=100):
        """Resize image while maintaining aspect ratio"""
        width, height = image.size
        # ASCII characters are taller than they are wide, so adjust aspect ratio
        aspect_ratio = height / width
        new_height = int(aspect_ratio * new_width * 0.55)  # 0.55 compensates for character height
        return image.resize((new_width, new_height))
    
    def grayscale_image(self, image):
        """Convert image to grayscale"""
        return image.convert("L")
    
    def enhance_contrast(self, image, factor=1.5):
        """Enhance image contrast for better ASCII conversion"""
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(factor)
    
    def pixels_to_ascii(self, image):
        """Convert image pixels to ASCII characters"""
        pixels = image.getdata()
        ascii_str = ""
        
        for pixel in pixels:
            # Map pixel intensity (0-255) to character index
            char_index = min(pixel * len(self.ascii_chars) // 256, len(self.ascii_chars) - 1)
            ascii_str += self.ascii_chars[char_index]
        
        return ascii_str
    
    def format_ascii(self, ascii_str, width):
        """Format ASCII string into lines based on image width"""
        ascii_lines = []
        for i in range(0, len(ascii_str), width):
            ascii_lines.append(ascii_str[i:i + width])
        return "\n".join(ascii_lines)
    
    def convert_image_to_ascii(self, image_path, width=100, contrast=1.5):
        """Main conversion function"""
        try:
            # Open and process image
            image = Image.open(image_path)
            
            # Resize image
            image = self.resize_image(image, width)
            
            # Convert to grayscale
            image = self.grayscale_image(image)
            
            # Enhance contrast
            image = self.enhance_contrast(image, contrast)
            
            # Convert to ASCII
            ascii_str = self.pixels_to_ascii(image)
            ascii_art = self.format_ascii(ascii_str, width)
            
            return ascii_art
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Image file '{image_path}' not found")
        except Exception as e:
            raise Exception(f"Error processing image: {str(e)}")
    
    def save_ascii_art(self, ascii_art, output_path):
        """Save ASCII art to file"""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(ascii_art)
            return True
        except Exception as e:
            print(f"Error saving ASCII art: {str(e)}")
            return False


def main():
    """Command line interface for ASCII art converter"""
    parser = argparse.ArgumentParser(
        description="Convert images to ASCII art using AI-like image processing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ascii_art_converter.py image.jpg
  python ascii_art_converter.py image.png --width 80 --output art.txt
  python ascii_art_converter.py photo.jpg --chars blocks --contrast 2.0
        """
    )
    
    parser.add_argument('image_path', help='Path to input image file')
    parser.add_argument('--width', '-w', type=int, default=100, 
                       help='Width of ASCII art in characters (default: 100)')
    parser.add_argument('--output', '-o', type=str, 
                       help='Output file path (prints to console if not specified)')
    parser.add_argument('--chars', '-c', choices=['detailed', 'simple', 'blocks'], 
                       default='detailed', help='Character set to use (default: detailed)')
    parser.add_argument('--contrast', type=float, default=1.5, 
                       help='Contrast enhancement factor (default: 1.5)')
    
    args = parser.parse_args()
    
    # Validate input file exists
    if not os.path.exists(args.image_path):
        print(f"Error: Image file '{args.image_path}' not found")
        sys.exit(1)
    
    # Create converter
    converter = ASCIIArtConverter(char_set=args.chars)
    
    try:
        # Convert image to ASCII art
        print(f"Converting '{args.image_path}' to ASCII art...")
        ascii_art = converter.convert_image_to_ascii(
            args.image_path, 
            width=args.width, 
            contrast=args.contrast
        )
        
        # Output results
        if args.output:
            if converter.save_ascii_art(ascii_art, args.output):
                print(f"ASCII art saved to '{args.output}'")
            else:
                sys.exit(1)
        else:
            print("\nASCII Art:")
            print("-" * args.width)
            print(ascii_art)
            print("-" * args.width)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()