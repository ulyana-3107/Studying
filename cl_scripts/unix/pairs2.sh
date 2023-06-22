#!/bin/bash

c=0 & c1=0 & c2=0 & even=0
for var in "$@" 
do
	c=$(($c + 1))
	res=$(($c % 2))
	if [ $res -eq 1 ]
	then
		if [ $c -eq $# ]
		then
			c1=$var
		       	c2=0
		       	even=1
		else
			c1=$var
		       	even=0
		fi
	else
		c2=$var
	       	even=1
	fi
	if [ $even -eq 1 ]
	then
		if [ $c1 -ge $c2 ]
		then
			param=$c1
		else
			param=$c2
		fi
		if [ $param -lt 0 ]
		then
			param=$(($param * $param))
		fi
		echo $param
	fi

done


