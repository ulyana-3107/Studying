#!/bin/bash

for i in "$@"; do
	res=$(./fib2.sh "$i")
	if [ $? -eq 0 ] 
	then
		echo $res
	else
		echo -1
	fi
done

