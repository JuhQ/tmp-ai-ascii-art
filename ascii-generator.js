class AsciiArtGenerator {
  constructor() {
    this.templates = {
      // Text-based ASCII art
      banner: this.createBanner.bind(this),
      block: this.createBlock.bind(this),
      
      // Predefined ASCII art
      animals: {
        cat: `
   /\\_/\\  
  ( o.o ) 
   > ^ <  `,
        dog: `
   / \\   / \\
  (   o.o   )
   \\  ___  /
    \\     /
     \\___/`,
        owl: `
    ,___,
    [O.o]
     )_)
    -"="-`,
        rabbit: `
      /|   /|  
     ( :v:  )
    o_("_")_o`,
        fish: `
    ><(((('>
       ><(('>`
      },
      
      faces: {
        happy: `
    :-D    :-)    :D    =D
    ^_^    (^_^)  \\o/   :-P`,
        sad: `
    :-(    :'(    ;_;   
    T_T    (._.)  ;-;`,
        surprised: `
    :-O    :o    O_O    @_@
    o.O    O.o   (o_O)`,
        wink: `
    ;-)    ;)    ^_-    ;P
    (^_~)  ;D    ;-P`
      },
      
      objects: {
        heart: `
    ♥♥♥♥♥♥♥♥♥♥♥♥♥
    ♥             ♥
    ♥  I ♥ ASCII  ♥
    ♥             ♥
    ♥♥♥♥♥♥♥♥♥♥♥♥♥`,
        star: `
        *
       ***
      *****
     *******
      *****
       ***
        *`,
        tree: `
        /\\
       /  \\
      /____\\
        ||
        ||`,
        house: `
        /\\
       /  \\
      /____\\
      |    |
      | __ |
      |____|`
      },
      
      symbols: {
        arrow_right: `
    ------>
    ======>
    >>>>>>>`,
        arrow_left: `
    <------
    <======
    <<<<<<<`,
        divider: `
    ==========================================
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ******************************************`,
        border: `
    ┌─────────────────────┐
    │                     │
    │    YOUR TEXT HERE   │
    │                     │
    └─────────────────────┘`
      }
    };
  }

  // Generate banner-style text
  createBanner(text) {
    if (!text) return "Please provide text for banner";
    
    const chars = {
      'A': [
        " ████ ",
        "██  ██",
        "██████",
        "██  ██",
        "██  ██"
      ],
      'B': [
        "██████",
        "██  ██",
        "██████",
        "██  ██",
        "██████"
      ],
      'C': [
        " █████",
        "██    ",
        "██    ",
        "██    ",
        " █████"
      ],
      'H': [
        "██  ██",
        "██  ██",
        "██████",
        "██  ██",
        "██  ██"
      ],
      'I': [
        "██████",
        "  ██  ",
        "  ██  ",
        "  ██  ",
        "██████"
      ],
      'L': [
        "██    ",
        "██    ",
        "██    ",
        "██    ",
        "██████"
      ],
      'O': [
        " █████",
        "██   ██",
        "██   ██",
        "██   ██",
        " █████"
      ],
      'R': [
        "██████",
        "██  ██",
        "██████",
        "██ ██ ",
        "██  ██"
      ],
      'T': [
        "██████",
        "  ██  ",
        "  ██  ",
        "  ██  ",
        "  ██  "
      ],
      'W': [
        "██   ██",
        "██   ██",
        "██ █ ██",
        "███████",
        "██   ██"
      ],
      ' ': [
        "      ",
        "      ",
        "      ",
        "      ",
        "      "
      ]
    };

    const lines = ["", "", "", "", ""];
    for (const char of text.toUpperCase()) {
      const charArt = chars[char] || chars[' '];
      for (let i = 0; i < 5; i++) {
        lines[i] += charArt[i] + " ";
      }
    }
    
    return lines.join('\\n');
  }

  // Generate block-style text
  createBlock(text) {
    if (!text) return "Please provide text for block";
    
    const border = "█".repeat(text.length + 4);
    return `${border}
█ ${text} █
${border}`;
  }

  // Get all available categories
  getCategories() {
    return Object.keys(this.templates).filter(key => typeof this.templates[key] === 'object');
  }

  // Get all items in a category
  getCategoryItems(category) {
    if (this.templates[category] && typeof this.templates[category] === 'object') {
      return Object.keys(this.templates[category]);
    }
    return [];
  }

  // Generate ASCII art by category and name
  generate(category, name, text = null) {
    if (category === 'banner' || category === 'block') {
      return this.templates[category](text);
    }
    
    if (this.templates[category] && this.templates[category][name]) {
      return this.templates[category][name];
    }
    
    return "ASCII art not found. Use listAll() to see available options.";
  }

  // List all available ASCII art
  listAll() {
    let result = "Available ASCII Art:\\n";
    result += "==================\\n\\n";
    
    result += "Text Generators:\\n";
    result += "- banner(text) - Create banner-style text\\n";
    result += "- block(text) - Create block-style text\\n\\n";
    
    for (const category of this.getCategories()) {
      result += `${category.toUpperCase()}:\\n`;
      for (const item of this.getCategoryItems(category)) {
        result += `- ${item}\\n`;
      }
      result += "\\n";
    }
    
    return result;
  }

  // Get random ASCII art
  getRandom() {
    const categories = this.getCategories();
    const randomCategory = categories[Math.floor(Math.random() * categories.length)];
    const items = this.getCategoryItems(randomCategory);
    const randomItem = items[Math.floor(Math.random() * items.length)];
    
    return {
      category: randomCategory,
      name: randomItem,
      art: this.generate(randomCategory, randomItem)
    };
  }

  // Generate multiple random ASCII arts
  getMultiple(count = 5) {
    const results = [];
    for (let i = 0; i < count; i++) {
      results.push(this.getRandom());
    }
    return results;
  }
}

module.exports = AsciiArtGenerator;