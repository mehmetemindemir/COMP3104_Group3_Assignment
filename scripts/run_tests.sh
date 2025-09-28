#!/bin/bash
# Test runner script for COMP3104 Group 3 Assignment

echo "Running tests for COMP3104 Group 3 Assignment..."
echo "================================================"

# Navigate to the project root
cd "$(dirname "$0")/.."

# Run Python tests
echo "Running Python tests..."
python3 -m pytest src/test/ -v

# Check if tests passed
if [ $? -eq 0 ]; then
    echo "✅ All tests passed!"
else
    echo "❌ Some tests failed!"
    exit 1
fi

echo "Test run complete."