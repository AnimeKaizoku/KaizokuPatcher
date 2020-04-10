@echo off

"%userprofile%\AppData\Local\Programs\Python\Python37\Scripts\pyinstaller" --onefile -n KaizokuPatcher --icon icon.ico --add-binary="xdelta3.exe;." patcher.py

move dist\KaizokuPatcher.exe .

del KaizokuPatcher.spec

rmdir /q /s dist
rmdir /q /s build
rmdir /q /s __pycache__

pause