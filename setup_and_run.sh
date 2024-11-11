#!/bin/bash

# Check for Python3 and pip3
if ! command -v python3 &>/dev/null || ! command -v pip3 &>/dev/null; then
  echo "Python3 and pip3 are required but not installed. Please install them first."
  exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
if [ -f "requirements.txt" ]; then
  echo "Installing dependencies from requirements.txt..."
  pip install -r requirements.txt
else
  echo "Error: requirements.txt not found!"
  exit 1
fi

# Apply migrations
echo "Applying database migrations..."
python3 hmoob_lus/manage.py migrate

# Run the Django development server
echo "Starting the Django development server..."
python3 hmoob_lus/manage.py runserver

echo "To stop the server, press Ctrl+C."
echo "To deactivate the virtual environment, run: deactivate"
