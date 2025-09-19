# tmp-ai-ascii-art

A Node.js generator that creates multiple markdown files featuring beautiful ASCII art designs.

## Features

- 🎨 Generates 8 different ASCII art designs
- 📝 Creates properly formatted markdown files
- 🗂️ Organizes files in a dedicated directory
- 📋 Includes an index file for easy navigation
- 🕒 Timestamps each generation

## Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/JuhQ/tmp-ai-ascii-art.git
   cd tmp-ai-ascii-art
   ```

2. **Run the generator**
   ```bash
   npm run generate
   ```
   or
   ```bash
   node generate.js
   ```

3. **View the generated files**
   The generator creates an `ascii-art-files/` directory containing:
   - 8 individual ASCII art markdown files
   - A README.md index file

## Generated ASCII Art Themes

- 🐱 **Cat** - Cute cat with whiskers
- 🐕 **Dog** - Friendly dog figure  
- ❤️ **Heart** - Romantic heart shape
- ⭐ **Star** - Bright shining star
- 🚀 **Rocket** - NASA space rocket
- 🎄 **Christmas Tree** - Festive tree with star
- 🏰 **Castle** - Medieval castle with towers
- 💻 **Computer** - Retro computer terminal

## File Structure

```
tmp-ai-ascii-art/
├── generate.js           # Main generator script
├── package.json         # Project configuration
├── README.md           # This file
└── ascii-art-files/    # Generated directory
    ├── README.md       # Index of all files
    ├── cat.md          # ASCII cat
    ├── dog.md          # ASCII dog
    ├── heart.md        # ASCII heart
    ├── star.md         # ASCII star
    ├── rocket.md       # ASCII rocket
    ├── tree.md         # ASCII tree
    ├── castle.md       # ASCII castle
    └── computer.md     # ASCII computer
```

## Customization

You can easily modify the `generate.js` file to:
- Add new ASCII art designs
- Change file names or descriptions
- Modify the markdown template
- Add different output formats

## Requirements

- Node.js (any recent version)
- No external dependencies required

## License

ISC