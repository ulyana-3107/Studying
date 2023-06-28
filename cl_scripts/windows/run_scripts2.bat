@echo off
set arg1=%1
set arg2=%2
type %arg1%| pairs.bat | fib_on_seq.bat >%arg2%
