#!/bin/bash
n=$1

if [ $n -le 0 ]; then
	exit 13
fi

a=1
b=1
i=2
while [ $i -lt $n ]; do
	c=$((a + b))
	a=$b
	b=$c
	i=$((i + 1))
done
echo $b
