#!/usr/bin/env node

const AsciiArtGenerator = require('./ascii-generator');
const generator = new AsciiArtGenerator();

// Simple command line interface
const args = process.argv.slice(2);

function showHelp() {
  console.log(`
🎨 ASCII Art Generator CLI
==========================

Usage:
  ascii-art [command] [options]

Commands:
  list                    - Show all available ASCII art
  random [count]         - Show random ASCII art (default: 1)
  banner <text>          - Generate banner text
  block <text>           - Generate block text
  get <category> <name>  - Get specific ASCII art
  demo                   - Show demo with examples

Examples:
  ascii-art list
  ascii-art random 3
  ascii-art banner "HELLO WORLD"
  ascii-art block "ASCII ART"
  ascii-art get animals cat
  ascii-art get faces happy
  ascii-art demo
`);
}

if (args.length === 0) {
  showHelp();
  process.exit(0);
}

const command = args[0];

switch (command) {
  case 'help':
  case '--help':
  case '-h':
    showHelp();
    break;
    
  case 'list':
    console.log(generator.listAll());
    break;
    
  case 'random':
    const count = parseInt(args[1]) || 1;
    const randoms = generator.getMultiple(count);
    randoms.forEach((item, index) => {
      console.log(`\\n🎲 Random #${index + 1} - ${item.category}/${item.name}:`);
      console.log(item.art);
    });
    break;
    
  case 'banner':
    if (!args[1]) {
      console.log("❌ Please provide text for banner");
      process.exit(1);
    }
    console.log(generator.generate('banner', null, args[1]));
    break;
    
  case 'block':
    if (!args[1]) {
      console.log("❌ Please provide text for block");
      process.exit(1);
    }
    console.log(generator.generate('block', null, args[1]));
    break;
    
  case 'get':
    if (!args[1] || !args[2]) {
      console.log("❌ Please provide category and name");
      console.log("Example: ascii-art get animals cat");
      process.exit(1);
    }
    const result = generator.generate(args[1], args[2]);
    console.log(result);
    break;
    
  case 'demo':
    require('./demo');
    break;
    
  default:
    console.log(`❌ Unknown command: ${command}`);
    showHelp();
    process.exit(1);
}