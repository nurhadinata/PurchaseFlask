where "bash.exe" >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
    set "GIT_BASH_PATH=bash.exe"
    echo Running the script using Git Bash...
    "%GIT_BASH_PATH%" --login -i "C:\Scripts\script.sh"
    echo Script executed.
) ELSE (
    echo Git Bash executable not found.
)
