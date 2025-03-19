#!/bin/bash
echo "Running tests..."
# TODO: Add commands to run unit and integration tests

# Install test dependencies (if any)
echo "Installing test dependencies..."
pip install -r requirements-test.txt  # Optional: If you have a separate requirements file for tests

# Run unit tests
echo "Running unit tests..."
pytest tests/unit -v  # Assumes unit tests are in the `tests/unit` directory

# Check if unit tests passed
if [ $? -ne 0 ]; then
    echo "Unit tests failed. Exiting."
    exit 1
fi

# Run integration tests
echo "Running integration tests..."
pytest tests/integration -v  # Assumes integration tests are in the `tests/integration` directory

# Check if integration tests passed
if [ $? -ne 0 ]; then
    echo "Integration tests failed. Exiting."
    exit 1
fi

echo "All tests passed successfully!"
