# 🎨 ASCII Art Generator - Much ASCII Art!

A comprehensive ASCII art generator with tons of templates, examples, and a simple CLI interface. Perfect for when you need **much ASCII art**!

## 🚀 Features

- 📝 **Text Generators**: Convert text to banner and block ASCII art
- 🐾 **Animals**: Cats, dogs, owls, rabbits, fish and more
- 😊 **Faces**: Happy, sad, surprised, wink expressions
- 🎯 **Objects**: Hearts, stars, trees, houses
- 🔣 **Symbols**: Arrows, dividers, borders
- 🎲 **Random Generation**: Get random ASCII art
- 💻 **CLI Interface**: Easy command-line usage
- 📦 **Module Export**: Use as a Node.js module

## 📦 Installation & Usage

### As a CLI tool:
```bash
# Run the demo
npm start

# Show comprehensive demo with ALL ASCII art
npm run demo

# Run tests
npm test

# CLI commands
node cli.js list                    # Show all available ASCII art
node cli.js random 5               # Show 5 random ASCII arts
node cli.js banner "HELLO WORLD"  # Generate banner text
node cli.js block "ASCII ART"     # Generate block text
node cli.js get animals cat       # Get specific ASCII art
node cli.js demo                  # Run full demo
```

### As a Node.js module:
```javascript
const generator = require('./ascii-generator');

// Generate banner text
console.log(generator.generate('banner', null, 'HELLO'));

// Get a cat
console.log(generator.generate('animals', 'cat'));

// Get random ASCII art
const random = generator.getRandom();
console.log(random.art);

// Get multiple random ASCII arts
const randoms = generator.getMultiple(5);
randoms.forEach(item => console.log(item.art));

// List all available ASCII art
console.log(generator.listAll());
```

## 🎨 Available ASCII Art Categories

### 📝 Text Generators
- **banner(text)** - Create large banner-style text
- **block(text)** - Create simple block-style text

### 🐾 Animals
- cat, dog, owl, rabbit, fish

### 😊 Faces  
- happy, sad, surprised, wink

### 🎯 Objects
- heart, star, tree, house

### 🔣 Symbols
- arrow_right, arrow_left, divider, border

## 🎲 Examples

### Banner Text:
```
 ████ 
██  ██
██████
██  ██
██  ██
```

### Animals:
```
   /\_/\  
  ( o.o ) 
   > ^ <  
```

### Objects:
```
        *
       ***
      *****
     *******
      *****
       ***
        *
```

## 🔧 API Reference

### Main Methods:
- `generate(category, name, text)` - Generate specific ASCII art
- `getRandom()` - Get random ASCII art
- `getMultiple(count)` - Get multiple random ASCII arts
- `listAll()` - List all available ASCII art
- `getCategories()` - Get all categories
- `getCategoryItems(category)` - Get items in a category

### CLI Commands:
- `list` - Show all available ASCII art
- `random [count]` - Show random ASCII art
- `banner <text>` - Generate banner text
- `block <text>` - Generate block text  
- `get <category> <name>` - Get specific ASCII art
- `demo` - Show comprehensive demo

## 🧪 Testing

Run the test suite:
```bash
npm test
```

The tests verify:
- Text generation (banner/block)
- ASCII art retrieval
- Random generation
- Error handling
- Category listing

## 💡 Perfect for:
- Terminal applications
- Console logging
- Text-based user interfaces
- Fun decorations in code comments
- README files
- CLI tool output
- And whenever you need **MUCH ASCII ART**! 🎉

## 📄 License

MIT License - Feel free to use this for all your ASCII art needs!