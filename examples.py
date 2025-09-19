#!/usr/bin/env python3
"""
Example script demonstrating the ASCII Art Generator
"""

from ascii_art_generator import ASCIIArtGenerator
import time

def main():
    print("=== ASCII Art Generator Demo ===\n")
    
    # Create a generator with smaller dimensions for demo
    generator = ASCIIArtGenerator(width=50, height=15)
    
    patterns = [
        ("Spiral Pattern", lambda: generator.spiral_pattern('*')),
        ("Wave Pattern", lambda: generator.wave_pattern('~')),
        ("Cellular Automata", lambda: generator.cellular_automata(30)),
        ("Random Stars", lambda: generator.random_stars(0.03)),
        ("Geometric Pattern", lambda: generator.geometric_pattern('+')),
        ("Circle Pattern", lambda: generator.circle_pattern('o')),
    ]
    
    for name, pattern_func in patterns:
        print(f"--- {name} ---")
        print(pattern_func())
        print("\n" + "="*50 + "\n")
        time.sleep(1)  # Small delay for visual effect

if __name__ == '__main__':
    main()