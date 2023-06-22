#!/bin/sh

if [ -n "${MY_VARIABLE+x}" ]; then
	echo $MY_VARIABLE
else
	echo MY_VARIABLE is not defined
	export MY_VARIABLE="default"
fi



