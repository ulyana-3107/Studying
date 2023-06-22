@echo off
set arg1=%1
set arg2=%2
type %arg1%| maxnumber.bat | fib_seq2.bat >%arg2%