@echo off
TITLE PyStark Batch Script File

@REM HELP
if "%1" == "help" set true=1
if "%1" == "" set true=1
if defined true (
    echo Usage: run [[delete^|docs^|test^|main]] [open]
    echo.
    echo 'test' - upload to test-pypi
    echo 'main' - upload to pypi
    echo 'docs' - only update docs
    echo 'delete' - only delete folders
    exit /b 0
)

@REM DELETE
echo [Deleting Unnecessary Folders]
set folder='dist'
rmdir dist /q/s && (
  echo Deleted %folder%
) || (
  echo Cannot found %folder%
)
set folder2='PyStark.egg-info'
rmdir PyStark.egg-info /q/s && (
  echo Deleted %folder2%
) || (
  echo Cannot found %folder2%
)
set folder3='docs/_build'
rmdir "docs/_build" /q/s && (
  echo Deleted %folder3%
) || (
  echo Cannot found %folder3%
)
if "%1" == "delete" exit /b 0
echo.

@REM DOCS
echo [Generating Docs]
call docs/make.bat html
if "%2" == "open" start docs/_build/html/index.html
if "%1" == "docs" exit /b 0
echo.

@REM DIST
echo [Creating Distribution Files]
python setup.py sdist
if "%1" == "dist" exit /b 0
echo.

@REM TEST/MAIN

if "%1" == "test" goto :test
if "%1" == "main" goto :main

:test
echo [Upload to TestPyPI]
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
echo.
echo [All Done]
exit /b 0

:main
echo [Upload to PyPI]
twine upload dist/*
echo.
echo [All Done]
exit /b 0

@REM To-Do : Create command-line tool using Python instead [*python developer lol*]
