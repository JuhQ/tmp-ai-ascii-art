# ASCII Tree Generator

A JavaScript program to generate beautiful ASCII trees based on customizable parameters.

## Features

- Generate ASCII trees with customizable height, characters, and trunk size
- Multiple tree styles: classic, christmas, and pine
- Command-line interface for easy usage
- Modular design for programmatic use

## Installation

```bash
git clone https://github.com/JuhQ/tmp-ai-ascii-art.git
cd tmp-ai-ascii-art
```

## Usage

### Command Line Interface

```bash
# Basic usage with default parameters
node index.js

# Custom height
node index.js --height 7

# Christmas tree style
node index.js --style christmas --height 6

# Pine tree style
node index.js --style pine --height 5

# Custom characters
node index.js --height 4 --leafChar @ --trunkChar #

# Custom trunk height
node index.js --height 6 --trunk 3
```

### Available Options

- `--height <number>`: Height of the tree (default: 5)
- `--style <string>`: Style of tree: classic, christmas, pine (default: classic)
- `--trunk <number>`: Height of trunk (default: 2)
- `--leafChar <char>`: Character for leaves (default: *)
- `--trunkChar <char>`: Character for trunk (default: |)
- `--help`: Show help message

### Programmatic Usage

```javascript
const AsciiTreeGenerator = require('./index.js');

// Create a tree with default parameters
const tree = new AsciiTreeGenerator();
console.log(tree.render());

// Create a custom tree
const customTree = new AsciiTreeGenerator({
  height: 7,
  style: 'christmas',
  leafChar: '🌲',
  trunk: 3
});
console.log(customTree.render());
```

## Examples

### Classic Tree
```
    *
   ***
  *****
 *******
*********
    |
    |
```

### Christmas Tree
```
      ★
      *
     ***
      *
     ***
    *****
      *
     ***
    *****
   *******
     |||
     |||
```

### Pine Tree
```
   ^
  /*\
 /***\
/*****\
   |
   |
```

### Custom Characters
```
    @
   @@@
  @@@@@
 @@@@@@@
@@@@@@@@@
    #
    #
    #
```

## Testing

Run the included tests to verify functionality:

```bash
npm test
# or
node test.js
```

## API Reference

### AsciiTreeGenerator Class

#### Constructor Options

- `height` (number): The height of the tree in rows
- `style` (string): The style of the tree ('classic', 'christmas', 'pine')
- `trunk` (number): The number of trunk rows
- `leafChar` (string): Character to use for leaves
- `trunkChar` (string): Character to use for trunk

#### Methods

- `generate()`: Generate a classic tree
- `generateChristmasTree()`: Generate a Christmas tree with star and layered sections
- `generatePineTree()`: Generate a pine tree with branch-like appearance
- `render()`: Generate tree based on the specified style

## License

MIT