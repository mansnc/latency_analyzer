@echo off
setlocal enabledelayedexpansion

REM Determine if we should use pip or pip3
for /f "tokens=2 delims= " %%i in ('python --version') do set PYTHON_VERSION=%%i
set PYTHON_MAJOR_VERSION=!PYTHON_VERSION:~0,1!

if !PYTHON_MAJOR_VERSION! EQU 3 (
    set PIP_COMMAND=pip3
) else (
    set PIP_COMMAND=pip
)

REM Check if pip is installed
%PIP_COMMAND% --version >nul 2>&1
if errorlevel 1 (
    echo %PIP_COMMAND% is not installed. Installing...
    python -m ensurepip --default-pip
) else (
echo %PIP_COMMAND% is installed; move on with packages installation
)


REM List of packages to check
set packages=statistics matplotlib scapy

for %%p in (%packages%) do (
    %PIP_COMMAND% list | findstr /C:"%%p" >nul
    if errorlevel 1 (
        echo %%p is not installed. Installing...
        %PIP_COMMAND% install %%p
    ) else (
        echo %%p is already installed.
    )
)

endlocal
pause
