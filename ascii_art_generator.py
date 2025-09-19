#!/usr/bin/env python3
"""
Generative ASCII Art Generator

This program creates various types of ASCII art patterns using algorithmic generation.
It includes multiple pattern types like spirals, fractals, waves, and geometric shapes.
"""

import random
import math
import argparse
import sys
from typing import List, Tuple, Callable


class ASCIIArtGenerator:
    """Main class for generating ASCII art patterns."""
    
    def __init__(self, width: int = 80, height: int = 24):
        self.width = width
        self.height = height
        self.canvas = [[' ' for _ in range(width)] for _ in range(height)]
    
    def clear_canvas(self):
        """Clear the canvas to all spaces."""
        self.canvas = [[' ' for _ in range(self.width)] for _ in range(self.height)]
    
    def set_pixel(self, x: int, y: int, char: str = '*'):
        """Set a character at the given coordinates if within bounds."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.canvas[y][x] = char
    
    def get_canvas_string(self) -> str:
        """Convert the canvas to a string representation."""
        return '\n'.join(''.join(row) for row in self.canvas)
    
    def spiral_pattern(self, char: str = '*') -> str:
        """Generate a spiral pattern."""
        self.clear_canvas()
        center_x, center_y = self.width // 2, self.height // 2
        
        for angle in range(0, 720, 2):  # Two full rotations
            radius = angle / 20.0
            x = int(center_x + radius * math.cos(math.radians(angle)))
            y = int(center_y + radius * math.sin(math.radians(angle)) * 0.5)  # Compress vertically
            self.set_pixel(x, y, char)
        
        return self.get_canvas_string()
    
    def wave_pattern(self, char: str = '~') -> str:
        """Generate a wave pattern."""
        self.clear_canvas()
        
        for x in range(self.width):
            # Create multiple waves with different frequencies
            y1 = int(self.height // 2 + 5 * math.sin(x * 0.2))
            y2 = int(self.height // 2 + 3 * math.sin(x * 0.3 + math.pi / 4))
            y3 = int(self.height // 2 + 2 * math.sin(x * 0.5 + math.pi / 2))
            
            self.set_pixel(x, y1, char)
            self.set_pixel(x, y2, '.')
            self.set_pixel(x, y3, '-')
        
        return self.get_canvas_string()
    
    def mandelbrot_pattern(self, char: str = '#') -> str:
        """Generate a simple Mandelbrot set visualization."""
        self.clear_canvas()
        
        max_iter = 20
        for py in range(self.height):
            for px in range(self.width):
                # Map pixel coordinates to complex plane
                x = (px - self.width // 2) * 3.0 / self.width
                y = (py - self.height // 2) * 2.0 / self.height
                
                c = complex(x, y)
                z = 0
                
                for i in range(max_iter):
                    if abs(z) > 2:
                        break
                    z = z * z + c
                
                if i < max_iter:
                    intensity_chars = ' .:-=+*#%@'
                    char_index = min(i * len(intensity_chars) // max_iter, len(intensity_chars) - 1)
                    self.set_pixel(px, py, intensity_chars[char_index])
        
        return self.get_canvas_string()
    
    def cellular_automata(self, rules: int = 30, generations: int = None) -> str:
        """Generate patterns using cellular automata (Rule 30 by default)."""
        self.clear_canvas()
        
        if generations is None:
            generations = self.height
        
        # Initialize first row with a single cell in the center
        current_row = [0] * self.width
        current_row[self.width // 2] = 1
        
        for gen in range(min(generations, self.height)):
            # Draw current generation
            for x in range(self.width):
                if current_row[x]:
                    self.set_pixel(x, gen, '#')
            
            # Calculate next generation
            next_row = [0] * self.width
            for i in range(self.width):
                left = current_row[(i - 1) % self.width]
                center = current_row[i]
                right = current_row[(i + 1) % self.width]
                
                # Apply rule (Rule 30 by default)
                pattern = (left << 2) | (center << 1) | right
                next_row[i] = (rules >> pattern) & 1
            
            current_row = next_row
        
        return self.get_canvas_string()
    
    def random_stars(self, density: float = 0.02, chars: str = '*+.') -> str:
        """Generate a random star field."""
        self.clear_canvas()
        
        num_stars = int(self.width * self.height * density)
        
        for _ in range(num_stars):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            char = random.choice(chars)
            self.set_pixel(x, y, char)
        
        return self.get_canvas_string()
    
    def geometric_pattern(self, char: str = '+') -> str:
        """Generate geometric patterns with intersecting lines."""
        self.clear_canvas()
        
        # Draw diagonal lines
        for i in range(max(self.width, self.height)):
            # Main diagonals
            if i < self.width and i < self.height:
                self.set_pixel(i, i, char)
            if i < self.width and (self.height - 1 - i) >= 0:
                self.set_pixel(i, self.height - 1 - i, char)
        
        # Draw grid pattern
        for y in range(0, self.height, 4):
            for x in range(self.width):
                self.set_pixel(x, y, '-')
        
        for x in range(0, self.width, 8):
            for y in range(self.height):
                self.set_pixel(x, y, '|')
        
        return self.get_canvas_string()
    
    def circle_pattern(self, char: str = 'o') -> str:
        """Generate concentric circles."""
        self.clear_canvas()
        
        center_x, center_y = self.width // 2, self.height // 2
        max_radius = min(center_x, center_y)
        
        for radius in range(2, max_radius, 3):
            for angle in range(0, 360, 2):
                x = int(center_x + radius * math.cos(math.radians(angle)))
                y = int(center_y + radius * math.sin(math.radians(angle)) * 0.5)  # Compress vertically
                self.set_pixel(x, y, char)
        
        return self.get_canvas_string()


def main():
    """Main function with command-line interface."""
    parser = argparse.ArgumentParser(description='Generate ASCII Art Patterns')
    parser.add_argument('pattern', nargs='?', default='spiral',
                       choices=['spiral', 'wave', 'mandelbrot', 'cellular', 'stars', 'geometric', 'circles', 'all'],
                       help='Type of pattern to generate')
    parser.add_argument('--width', type=int, default=80, help='Canvas width (default: 80)')
    parser.add_argument('--height', type=int, default=24, help='Canvas height (default: 24)')
    parser.add_argument('--char', type=str, default='*', help='Character to use for drawing')
    
    args = parser.parse_args()
    
    generator = ASCIIArtGenerator(args.width, args.height)
    
    patterns = {
        'spiral': lambda: generator.spiral_pattern(args.char),
        'wave': lambda: generator.wave_pattern(args.char),
        'mandelbrot': lambda: generator.mandelbrot_pattern(),
        'cellular': lambda: generator.cellular_automata(),
        'stars': lambda: generator.random_stars(),
        'geometric': lambda: generator.geometric_pattern(args.char),
        'circles': lambda: generator.circle_pattern(args.char)
    }
    
    if args.pattern == 'all':
        print("=== ASCII Art Gallery ===\n")
        for name, pattern_func in patterns.items():
            print(f"--- {name.upper()} PATTERN ---")
            print(pattern_func())
            print("\n" + "="*args.width + "\n")
    else:
        if args.pattern in patterns:
            print(patterns[args.pattern]())
        else:
            print(f"Unknown pattern: {args.pattern}")
            sys.exit(1)


if __name__ == '__main__':
    main()