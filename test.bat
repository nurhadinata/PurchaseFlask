@echo off

REM echo Installing Git Bash...
REM winget install --id Git.Git -e

REM winget install --id Google.Chrome -e
set "GIT_BASH_PATH=C:\Program Files\Git\bin\bash.exe"
set "SCRIPT_PATH=C:\Scripts\test.sh"
start "" "%GIT_BASH_PATH%" "%SCRIPT_PATH%"
