@echo off
echo ========================================================
echo         Building JARVIS Production-Ready Executable
echo ========================================================
echo.

:: Clean previous builds
echo Cleaning previous builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist Jarvis.spec del /q Jarvis.spec
if exist app.spec del /q app.spec
echo Clean complete.
echo.

:: Detect virtual environment
set PYTHON_EXE=python
if exist ".venv\Scripts\python.exe" (
    echo Detected local virtual environment.
    set PYTHON_EXE=.venv\Scripts\python.exe
) else (
    echo Using global Python environment.
)

:: Build the executable
echo Running PyInstaller to build JARVIS in 'onedir' mode...
echo.
"%PYTHON_EXE%" -m PyInstaller --noconfirm --noconsole --onedir --name="Jarvis" --icon="frontend/assets/jarvis_logo.ico" --add-data "frontend;frontend" app.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Build failed. Please verify that all dependencies are installed.
    exit /b %ERRORLEVEL%
)

echo.
echo ========================================================
echo                   BUILD COMPLETED SUCCESSFULLY!
echo ========================================================
echo.
echo Output executable is located at:
echo dist\Jarvis\Jarvis.exe
echo.
