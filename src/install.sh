#!/bin/bash
echo "Installing F1 Results Tracker"
echo "Checking if Python is installed"

sleep 1

if ! [[ -x "$(command -v python3)" ]];
then
    echo "Python 3 is not installed. Please install it before running this script.
    To install Python, follow the instructions at https://www.python.org/downloads/" >&2
    exit 1
fi

echo "Installing dependencies"

python3 -m venv venv
source ./venv/bin/activate
./venv/bin/pip install -r requirements.txt
deactivate

echo ""
echo "Done!"
echo ""

echo "If you want to run the application now, type './run.sh'"