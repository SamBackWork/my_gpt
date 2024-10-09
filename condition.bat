@echo off
if exist ".venv\" (
    call .venv\Scripts\activate.bat
	call python main.py
) else (
	call python -m venv .venv
	call .venv\Scripts\activate.bat
	call python.exe -m pip install --upgrade pip
	call pip install -r requirements.txt
	call python main.py
)