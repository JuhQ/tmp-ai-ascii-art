#!/usr/bin/env node

class AsciiTreeGenerator {
  constructor(options = {}) {
    this.height = options.height || 5;
    this.style = options.style || 'classic';
    this.trunk = options.trunk || 2;
    this.leafChar = options.leafChar || '*';
    this.trunkChar = options.trunkChar || '|';
  }

  /**
   * Generate an ASCII tree based on the configured parameters
   * @returns {string} The ASCII tree as a string
   */
  generate() {
    let tree = '';
    
    // Generate the tree crown/leaves
    for (let i = 0; i < this.height; i++) {
      const width = (i * 2) + 1;
      const spaces = ' '.repeat(this.height - i - 1);
      const leaves = this.leafChar.repeat(width);
      tree += spaces + leaves + '\n';
    }
    
    // Generate the trunk
    const trunkSpaces = ' '.repeat(this.height - 1);
    for (let i = 0; i < this.trunk; i++) {
      tree += trunkSpaces + this.trunkChar + '\n';
    }
    
    return tree;
  }

  /**
   * Generate a Christmas tree style
   * @returns {string} The Christmas tree as a string
   */
  generateChristmasTree() {
    let tree = '';
    
    // Star on top
    const starSpaces = ' '.repeat(this.height);
    tree += starSpaces + '★' + '\n';
    
    // Generate layered tree sections
    for (let section = 0; section < 3; section++) {
      const sectionHeight = Math.ceil(this.height / 3) + section;
      for (let i = 0; i < sectionHeight; i++) {
        const width = (i * 2) + 1;
        const spaces = ' '.repeat(this.height - i);
        const leaves = this.leafChar.repeat(width);
        tree += spaces + leaves + '\n';
      }
    }
    
    // Generate the trunk
    const trunkSpaces = ' '.repeat(this.height - 1);
    for (let i = 0; i < this.trunk; i++) {
      tree += trunkSpaces + this.trunkChar + this.trunkChar + this.trunkChar + '\n';
    }
    
    return tree;
  }

  /**
   * Generate a pine tree style with branches
   * @returns {string} The pine tree as a string
   */
  generatePineTree() {
    let tree = '';
    
    for (let i = 0; i < this.height; i++) {
      const width = (i * 2) + 1;
      const spaces = ' '.repeat(this.height - i - 1);
      
      if (width === 1) {
        tree += spaces + '^' + '\n';
      } else {
        const leaves = '/';
        const middle = this.leafChar.repeat(width - 2);
        const endLeaves = '\\';
        tree += spaces + leaves + middle + endLeaves + '\n';
      }
    }
    
    // Generate the trunk
    const trunkSpaces = ' '.repeat(this.height - 1);
    for (let i = 0; i < this.trunk; i++) {
      tree += trunkSpaces + this.trunkChar + '\n';
    }
    
    return tree;
  }

  /**
   * Generate tree based on style
   * @returns {string} The generated tree
   */
  render() {
    switch (this.style) {
      case 'christmas':
        return this.generateChristmasTree();
      case 'pine':
        return this.generatePineTree();
      case 'classic':
      default:
        return this.generate();
    }
  }
}

// CLI functionality
function parseArgs() {
  const args = process.argv.slice(2);
  const options = {};
  
  for (let i = 0; i < args.length; i += 2) {
    const key = args[i].replace('--', '');
    const value = args[i + 1];
    
    if (key === 'height' || key === 'trunk') {
      options[key] = parseInt(value, 10);
    } else {
      options[key] = value;
    }
  }
  
  return options;
}

function showHelp() {
  console.log(`ASCII Tree Generator

Usage: node index.js [options]

Options:
  --height <number>    Height of the tree (default: 5)
  --style <string>     Style of tree: classic, christmas, pine (default: classic)
  --trunk <number>     Height of trunk (default: 2)
  --leafChar <char>    Character for leaves (default: *)
  --trunkChar <char>   Character for trunk (default: |)
  --help               Show this help message

Examples:
  node index.js --height 7 --style christmas
  node index.js --height 4 --leafChar @ --trunkChar #
  node index.js --style pine --height 6 --trunk 3
`);
}

// Main execution
if (require.main === module) {
  const args = process.argv.slice(2);
  
  if (args.includes('--help') || args.includes('-h')) {
    showHelp();
    process.exit(0);
  }
  
  const options = parseArgs();
  const generator = new AsciiTreeGenerator(options);
  console.log(generator.render());
}

module.exports = AsciiTreeGenerator;