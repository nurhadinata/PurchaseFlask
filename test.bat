@echo off
setlocal

REM Check if winget is already installed
where winget >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
    echo winget is already installed and available in the PATH.
    goto :end
)

REM Determine the location of the App Installer package (winget)
echo Checking Windows version...
ver | findstr /I "10.0.19041" >nul
IF %ERRORLEVEL% NEQ 0 (
    echo This script requires Windows 10 version 2004 (10.0.19041) or later.
    pause
    exit /b 1
)

REM Install App Installer from Microsoft Store
echo Installing App Installer (winget)...
start ms-windows-store://pdp/?productid=9nblggh4nns1

REM Wait for user to install from Store
echo Please install the App Installer from the Microsoft Store.
pause

REM Verify winget installation
where winget >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo winget is not installed. Please install it from the Microsoft Store and rerun this script.
    pause
    exit /b 1
)

REM Find the actual winget executable path
set WINGET_PATH=""
for /f "delims=" %%I in ('dir /s /b "%ProgramFiles%\WindowsApps\Microsoft.DesktopAppInstaller_*\winget.exe" 2^>nul') do (
    set WINGET_PATH=%%I
    goto :found
)
:found

REM Add winget to system PATH
IF NOT "%WINGET_PATH%"=="" (
    echo Adding winget to system PATH...
    setx PATH "%PATH%;%WINGET_PATH%"
    echo winget has been added to the system PATH. Please restart your Command Prompt.
) ELSE (
    echo winget executable not found. Please ensure it is installed correctly.
    pause
    exit /b 1
)

:end
pause
endlocal
exit /b 0
