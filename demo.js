const AsciiArtGenerator = require('./ascii-generator');

const generator = new AsciiArtGenerator();

console.log("🎨 MUCH ASCII ART - Comprehensive Demo");
console.log("=====================================\\n");

// Banner examples
console.log("📝 BANNER TEXT EXAMPLES:");
console.log("========================");
const bannerTexts = ['ASCII', 'ART', 'HELLO', 'WORLD'];
bannerTexts.forEach(text => {
  console.log(`\\n--- ${text} ---`);
  console.log(generator.generate('banner', null, text));
});

console.log("\\n\\n📦 BLOCK TEXT EXAMPLES:");
console.log("=======================");
const blockTexts = ['COOL', 'AWESOME', 'FANTASTIC', 'AMAZING'];
blockTexts.forEach(text => {
  console.log(`\\n--- ${text} ---`);
  console.log(generator.generate('block', null, text));
});

console.log("\\n\\n🐾 ALL ANIMALS:");
console.log("===============");
generator.getCategoryItems('animals').forEach(animal => {
  console.log(`\\n--- ${animal.toUpperCase()} ---`);
  console.log(generator.generate('animals', animal));
});

console.log("\\n\\n😊 ALL FACES:");
console.log("=============");
generator.getCategoryItems('faces').forEach(face => {
  console.log(`\\n--- ${face.toUpperCase()} ---`);
  console.log(generator.generate('faces', face));
});

console.log("\\n\\n🎯 ALL OBJECTS:");
console.log("===============");
generator.getCategoryItems('objects').forEach(object => {
  console.log(`\\n--- ${object.toUpperCase()} ---`);
  console.log(generator.generate('objects', object));
});

console.log("\\n\\n🔣 ALL SYMBOLS:");
console.log("===============");
generator.getCategoryItems('symbols').forEach(symbol => {
  console.log(`\\n--- ${symbol.toUpperCase()} ---`);
  console.log(generator.generate('symbols', symbol));
});

console.log("\\n\\n🎲 10 RANDOM ASCII ARTS:");
console.log("=========================");
const randoms = generator.getMultiple(10);
randoms.forEach((item, index) => {
  console.log(`\\n--- RANDOM #${index + 1}: ${item.category}/${item.name} ---`);
  console.log(item.art);
});

console.log("\\n\\n🎊 MUCH ASCII ART COMPLETE!");
console.log("============================");
console.log("You now have access to tons of ASCII art! 🎉");
console.log("\\nUse the CLI commands to generate more:");
console.log("- node cli.js random 5");
console.log("- node cli.js banner \\"YOUR TEXT\\"");
console.log("- node cli.js get animals cat");
console.log("- node cli.js list");