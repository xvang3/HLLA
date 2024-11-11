@echo off

:: Check if Python3 is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python3 is required but not installed. Please install it first.
    exit /b 1
)

:: Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Install dependencies
if exist "requirements.txt" (
    echo Installing dependencies from requirements.txt...
    pip install -r requirements.txt
) else (
    echo Error: requirements.txt not found!
    exit /b 1
)

:: Apply migrations
echo Applying database migrations...
python hmoob_lus/manage.py migrate

:: Run the Django development server
echo Starting the Django development server...
python hmoob_lus/manage.py runserver

echo To stop the server, press Ctrl+C.
