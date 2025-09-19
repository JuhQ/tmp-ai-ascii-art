const AsciiArtGenerator = require('./ascii-generator');

function runTests() {
  const generator = new AsciiArtGenerator();
  let passed = 0;
  let failed = 0;

  console.log("🧪 Running ASCII Art Generator Tests");
  console.log("===================================\\n");

  // Test 1: Banner generation
  try {
    const banner = generator.generate('banner', null, 'HI');
    if (banner.includes('██') && banner.includes('\\n')) {
      console.log("✅ Test 1 PASSED: Banner generation works");
      passed++;
    } else {
      console.log("❌ Test 1 FAILED: Banner generation failed");
      failed++;
    }
  } catch (e) {
    console.log("❌ Test 1 FAILED: Banner generation threw error:", e.message);
    failed++;
  }

  // Test 2: Block generation
  try {
    const block = generator.generate('block', null, 'TEST');
    if (block.includes('█') && block.includes('TEST')) {
      console.log("✅ Test 2 PASSED: Block generation works");
      passed++;
    } else {
      console.log("❌ Test 2 FAILED: Block generation failed");
      failed++;
    }
  } catch (e) {
    console.log("❌ Test 2 FAILED: Block generation threw error:", e.message);
    failed++;
  }

  // Test 3: Animal ASCII art
  try {
    const cat = generator.generate('animals', 'cat');
    if (cat.includes('o.o') || cat.includes('/\\\\_/\\\\')) {
      console.log("✅ Test 3 PASSED: Animal ASCII art works");
      passed++;
    } else {
      console.log("❌ Test 3 FAILED: Animal ASCII art failed");
      failed++;
    }
  } catch (e) {
    console.log("❌ Test 3 FAILED: Animal ASCII art threw error:", e.message);
    failed++;
  }

  // Test 4: Categories listing
  try {
    const categories = generator.getCategories();
    if (categories.includes('animals') && categories.includes('faces') && 
        categories.includes('objects') && categories.includes('symbols')) {
      console.log("✅ Test 4 PASSED: Categories listing works");
      passed++;
    } else {
      console.log("❌ Test 4 FAILED: Categories listing failed");
      failed++;
    }
  } catch (e) {
    console.log("❌ Test 4 FAILED: Categories listing threw error:", e.message);
    failed++;
  }

  // Test 5: Random generation
  try {
    const random = generator.getRandom();
    if (random.category && random.name && random.art) {
      console.log("✅ Test 5 PASSED: Random generation works");
      passed++;
    } else {
      console.log("❌ Test 5 FAILED: Random generation failed");
      failed++;
    }
  } catch (e) {
    console.log("❌ Test 5 FAILED: Random generation threw error:", e.message);
    failed++;
  }

  // Test 6: Multiple random generation
  try {
    const randoms = generator.getMultiple(3);
    if (randoms.length === 3 && randoms.every(r => r.category && r.name && r.art)) {
      console.log("✅ Test 6 PASSED: Multiple random generation works");
      passed++;
    } else {
      console.log("❌ Test 6 FAILED: Multiple random generation failed");
      failed++;
    }
  } catch (e) {
    console.log("❌ Test 6 FAILED: Multiple random generation threw error:", e.message);
    failed++;
  }

  // Test 7: List all functionality
  try {
    const list = generator.listAll();
    if (list.includes('Available ASCII Art') && list.includes('ANIMALS') && list.includes('FACES')) {
      console.log("✅ Test 7 PASSED: List all functionality works");
      passed++;
    } else {
      console.log("❌ Test 7 FAILED: List all functionality failed");
      failed++;
    }
  } catch (e) {
    console.log("❌ Test 7 FAILED: List all functionality threw error:", e.message);
    failed++;
  }

  // Test 8: Error handling
  try {
    const invalid = generator.generate('invalid', 'invalid');
    if (invalid.includes('not found')) {
      console.log("✅ Test 8 PASSED: Error handling works");
      passed++;
    } else {
      console.log("❌ Test 8 FAILED: Error handling failed");
      failed++;
    }
  } catch (e) {
    console.log("❌ Test 8 FAILED: Error handling threw error:", e.message);
    failed++;
  }

  console.log(`\\n📊 Test Results:`);
  console.log(`✅ Passed: ${passed}`);
  console.log(`❌ Failed: ${failed}`);
  console.log(`📈 Success Rate: ${((passed / (passed + failed)) * 100).toFixed(1)}%`);

  if (failed === 0) {
    console.log("\\n🎉 All tests passed! ASCII Art Generator is working perfectly!");
    return true;
  } else {
    console.log("\\n⚠️  Some tests failed. Please check the implementation.");
    return false;
  }
}

// Run tests if called directly
if (require.main === module) {
  runTests();
}

module.exports = runTests;