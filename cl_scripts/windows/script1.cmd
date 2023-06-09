@echo off
if defined MY_VARIABLE (echo %MY_VARIABLE%) else (echo MY_VARIABLE is not defined)
set MY_VARIABLE=default
