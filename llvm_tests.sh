#!/bin/bash

# Compiler command, adjust it according to your setup
COMPILER_COMMAND="python -m compiler --input"
# Directory containing your C files for testing, adjusted to focus on "man_pass" files
TEST_FILES_DIR="input"
# Output directory for any compiler outputs
OUTPUT_DIR="output"

# Check if output directory exists, if not create it
if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir -p "$OUTPUT_DIR"
fi

# Counter for passed and failed tests
PASSED=0
FAILED=0

# Iterate over each .c file in the test files directory that contains "man_pass" in the filename
for FILE in $TEST_FILES_DIR/*man_pass*.c; do
  # Extracting filename for output naming
  FILENAME=$(basename "$FILE" .c)

  # Run the compiler command on the file
  $COMPILER_COMMAND "$FILE" --render_ast "$OUTPUT_DIR" --no-optimise --target_llvm "$OUTPUT_DIR" > "$OUTPUT_DIR/${FILENAME}_compile_output.txt" 2>&1

  # Check the exit status of the last command (compiler command)
  if [ $? -eq 0 ]; then
    echo "Test case $FILENAME passed."
    ((PASSED++))
  else
    echo "Test case $FILENAME failed. Check $OUTPUT_DIR/${FILENAME}_compile_output.txt for details."
    ((FAILED++))
  fi
done

# Summary
echo "Total passed: $PASSED"
echo "Total failed: $FAILED"
