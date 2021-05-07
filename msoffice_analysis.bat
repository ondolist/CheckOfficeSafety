@echo off
echo.
echo.
echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
echo.
echo.
oleid %1
call :decorate

olevba -d %1
call :decorate

mraptor %1
call :decorate

msodde -a %1
call :decorate

pyxswf %1
call :decorate

rtfobj %1
call :decorate

python url_extractor.py %1
call :decorate

pause
goto :eof

:decorate
echo.
echo.
echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
echo.
echo.
EXIT /B 0


:eof
