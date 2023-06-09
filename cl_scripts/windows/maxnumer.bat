@echo off

setlocal enabledelayedexpansion

set arg1=
set arg2=

for %%i in (%*) do (
if not defined arg1 (
set arg1=%%i
) else (
set arg2=%%i
if !arg1! geq !arg2! (
if !arg1! LSS 0 (set /a ad=!arg1!*!arg1!) else (set /a ad=!arg1!)
echo !ad! >> output.txt
) else (
if !arg2! LSS 0 (set /a ad=!arg2!*!arg2!) else (set /a ad=!arg2!)
echo !ad! >> output.txt
)
set arg1=
set arg2=
)
)
if defined arg1 (
set arg2=0
if !arg1! geq !arg2! (
if !arg1! LSS 0 (set /a ad=!arg1!*!arg1!) else (set /a ad=!arg1!)
echo !ad! >> output.txt
) else (
if !arg2! LSS 0 (set /a ad=!arg2!*!arg2!) else (set /a ad=!arg2!)
echo !ad! >> output.txt
)
)
)