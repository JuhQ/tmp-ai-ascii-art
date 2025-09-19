const AsciiTreeGenerator = require('./index.js');

function test(testName, actual, expected) {
  if (actual === expected) {
    console.log(`✅ ${testName}: PASSED`);
  } else {
    console.log(`❌ ${testName}: FAILED`);
    console.log(`Expected:\n${expected}`);
    console.log(`Actual:\n${actual}`);
  }
}

function runTests() {
  console.log('Running ASCII Tree Generator Tests...\n');

  // Test 1: Basic tree with default parameters
  const basicTree = new AsciiTreeGenerator();
  const basicOutput = basicTree.generate();
  const expectedBasic = `    *
   ***
  *****
 *******
*********
    |
    |
`;
  test('Basic tree generation', basicOutput, expectedBasic);

  // Test 2: Custom height
  const customHeight = new AsciiTreeGenerator({ height: 3 });
  const customHeightOutput = customHeight.generate();
  const expectedCustomHeight = `  *
 ***
*****
  |
  |
`;
  test('Custom height tree', customHeightOutput, expectedCustomHeight);

  // Test 3: Custom characters
  const customChars = new AsciiTreeGenerator({ 
    height: 3, 
    leafChar: '@', 
    trunkChar: '#',
    trunk: 1
  });
  const customCharsOutput = customChars.generate();
  const expectedCustomChars = `  @
 @@@
@@@@@
  #
`;
  test('Custom characters tree', customCharsOutput, expectedCustomChars);

  // Test 4: Pine tree style
  const pineTree = new AsciiTreeGenerator({ height: 4, style: 'pine' });
  const pineOutput = pineTree.generatePineTree();
  const expectedPine = `   ^
  /*\\
 /***\\
/*****\\
   |
   |
`;
  test('Pine tree style', pineOutput, expectedPine);

  console.log('\n🎄 All tests completed!');
}

if (require.main === module) {
  runTests();
}