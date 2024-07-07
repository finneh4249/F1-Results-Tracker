@echo off
echo Installing F1 Results Tracker
echo Checking if Python is installed

ping -n 2 127.0.0.1 >nul

where python3 >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3 is not installed. Please install it before running this script.
    echo To install Python, follow the instructions at https://www.python.org/downloads/
    exit /b 1
)

echo Installing dependencies

python3 -m venv venv
call venv\Scripts\activate
venv\Scripts\pip install -r requirements.txt
call deactivate

echo Done!
echo.
echo If you want to run the application now, type '.\\run.bat'
