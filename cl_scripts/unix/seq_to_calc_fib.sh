#!/bin/bash
for elem in "$@"; do
        res=$(./fib.sh "$elem")
        if [ $? -eq 0 ]
        then
                echo $res
        else
                echo "-1"
        fi
done
