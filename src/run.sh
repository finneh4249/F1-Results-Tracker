#!/bin/bash

echo "Starting F1 Results Tracker"
python3 -m venv venv
source ./venv/bin/activate

python3 main.py $1

deactivate
