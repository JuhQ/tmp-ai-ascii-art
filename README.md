# tmp-ai-ascii-art

A Python program that generates various types of ASCII art using algorithmic patterns and mathematical functions.

## Features

- **Spiral Patterns**: Create beautiful spiraling designs
- **Wave Patterns**: Generate wave-like patterns with multiple frequencies
- **Mandelbrot Set**: ASCII visualization of the famous fractal
- **Cellular Automata**: Rule-based generative patterns (Rule 30 by default)
- **Random Stars**: Scattered star field patterns
- **Geometric Patterns**: Grid-based geometric designs
- **Circle Patterns**: Concentric circle designs

## Usage

### Command Line Interface

```bash
# Generate a spiral pattern
python3 ascii_art_generator.py spiral

# Generate a wave pattern with custom dimensions
python3 ascii_art_generator.py wave --width 60 --height 20

# Generate Mandelbrot set
python3 ascii_art_generator.py mandelbrot --width 80 --height 24

# Generate cellular automata pattern
python3 ascii_art_generator.py cellular

# Generate random stars
python3 ascii_art_generator.py stars

# Generate geometric pattern with custom character
python3 ascii_art_generator.py geometric --char '#'

# Generate concentric circles
python3 ascii_art_generator.py circles

# Show all patterns
python3 ascii_art_generator.py all

# Get help
python3 ascii_art_generator.py --help
```

### Parameters

- `pattern`: Choose from `spiral`, `wave`, `mandelbrot`, `cellular`, `stars`, `geometric`, `circles`, or `all`
- `--width`: Canvas width (default: 80)
- `--height`: Canvas height (default: 24)
- `--char`: Character to use for drawing (default: '*')

### As a Library

```python
from ascii_art_generator import ASCIIArtGenerator

# Create generator
generator = ASCIIArtGenerator(width=80, height=24)

# Generate patterns
spiral = generator.spiral_pattern('*')
wave = generator.wave_pattern('~')
mandelbrot = generator.mandelbrot_pattern()

print(spiral)
```

## Examples

Run the examples script to see all patterns in action:

```bash
python3 examples.py
```

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Pattern Details

### Spiral Pattern
Creates a mathematical spiral using trigonometric functions.

### Wave Pattern
Generates multiple sine waves with different frequencies and phases.

### Mandelbrot Set
Renders the famous fractal using iteration over complex numbers.

### Cellular Automata
Implements Rule 30 (or custom rules) for generating complex patterns from simple rules.

### Random Stars
Creates a random distribution of star characters.

### Geometric Pattern
Draws intersecting lines and grid patterns.

### Circle Pattern
Generates concentric circles using trigonometric calculations.