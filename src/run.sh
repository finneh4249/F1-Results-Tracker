# sudo apt install python3.10-venv
#!/bin/bash

python3 -m venv venv
source ./venv/bin/activate
./venv/bin/pip install -r requirements.txt

python3 main.py

deactivate
