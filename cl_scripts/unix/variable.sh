#!/bin/bash

if [ -z "${MY_VARIABLE}" ];
then
	MY_VARIABLE="default"
	echo $MY_VARIABLE
else
	echo "${MY_VARIABLE}"
fi