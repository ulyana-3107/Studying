@Echo Off
If "%1"=="" (Exit /B 2)
If %1 LSS 1 (Exit /B 13)
        
Set /A i1=0, i2=1
    
If %1 EQU 1 Echo  N=%1;     Fibonacci Number=%i1% & Exit /B 0
If %1 EQU 2 Echo  N=%1;     Fibonacci Number=%i2% & Exit /B 0
        
For /L %%f In (3,1,%1) Do (
Call Set /A m=%%i2%%, i2+=%%i1%%
Call Set /A i1=%%m%%, Fib=%%i2%%  
)
Echo  N=%1;     Fibonacci Number=%i2%
Exit /B
