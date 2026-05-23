REM Check if the repository is already initialized
if not exist .git (
    git init
    if errorlevel 1 (
        echo Failed to initialize Git repository.
        exit /b 1
    )
)

REM Remove existing remote origin if it exists
git remote remove origin 2>nul

REM Add new remote origin
git remote add origin https://github.com/Mahesh9645/Python_Test_Automation.git
if errorlevel 1 (
    echo Failed to add remote origin.
    exit /b 1
)

git status
pause

git add .
if errorlevel 1 (
    echo Failed to stage changes.
    exit /b 1
)

pause

git status

git commit -m "Initial commit or update"
if errorlevel 1 (
    echo Failed to commit changes.
    exit /b 1
)

pause

git push origin main
if errorlevel 1 (
    echo Failed to push changes to remote repository.
    exit /b 1
)

pause

git status