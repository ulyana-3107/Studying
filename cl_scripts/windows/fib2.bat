@echo off

call :factorial %1
echo %result%
exit /b

: factorial
if %1 LEQ 0 (
EXIT /B 13
)
if %1 == 1 (
set result=1
exit /b
)
if %1 == 2 (
set result=1
exit /b
)
set /a a=1
set /a b=1
set /a c=2

:do
set /a c+=1
set /a temp=%b%
set /a b=%a%+%b%
set /a a=%temp%
:while 
if %c% geq %1 (goto next) else (goto do)
:next
set /a result=%b%













 