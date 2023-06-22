@ echo off
if defined MY_VARIABLE (
echo %MY_VARIABLE%
) else if not defined MY_VARIABLE (
echo MY_VARIABLE is not defined
set MY_VARIABLE=default
)
