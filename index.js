const AsciiArtGenerator = require('./ascii-generator');

const generator = new AsciiArtGenerator();

// Export the generator for use as a module
module.exports = generator;

// If run directly, show demo
if (require.main === module) {
  console.log("🎨 ASCII Art Generator Demo");
  console.log("===========================\\n");
  
  // Show some examples
  console.log("📝 BANNER TEXT:");
  console.log(generator.generate('banner', null, 'HELLO'));
  console.log("\\n");
  
  console.log("🐱 ANIMALS:");
  console.log(generator.generate('animals', 'cat'));
  console.log("\\n");
  
  console.log("😊 FACES:");
  console.log(generator.generate('faces', 'happy'));
  console.log("\\n");
  
  console.log("⭐ OBJECTS:");
  console.log(generator.generate('objects', 'star'));
  console.log("\\n");
  
  console.log("🎲 RANDOM ASCII ART:");
  const random = generator.getRandom();
  console.log(`Category: ${random.category}, Name: ${random.name}`);
  console.log(random.art);
  console.log("\\n");
  
  console.log("📋 Available ASCII Art:");
  console.log(generator.listAll());
}