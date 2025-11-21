@echo off
pip install pyinstaller customtkinter matplotlib
pyinstaller --onefile --add-data "ui;ui" --add-data "data;data" --add-data "assets;assets" main.py
echo Done. See dist folder.
pause
