echo Installing Git Bash...
REM Change the URL to the latest Git Bash installer URL
set installerUrl=https://github.com/git-for-windows/git/releases/download/v2.34.0.windows.2/Git-2.34.0.2-64-bit.exe
set installerPath=%TEMP%\GitInstaller.exe

REM Download Git Bash installer
echo Downloading Git Bash installer from %installerUrl%...
powershell -command "(New-Object System.Net.WebClient).DownloadFile('%installerUrl%', '%installerPath%')"

REM Install Git Bash
echo Installing Git Bash...
start "" /wait "%installerPath%" /SILENT /NORESTART

REM Clean up installer
echo Cleaning up...
del "%installerPath%"

echo Git Bash installation complete.
