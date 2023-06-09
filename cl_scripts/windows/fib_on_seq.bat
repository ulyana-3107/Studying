@echo off 
for %%i in (%*) do (
   call fib.bat %%i
   if errorlevel 1 echo -1
)
