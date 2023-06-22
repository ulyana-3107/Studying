#!/bin/bash

arg1=$1
arg2=$2

cat $arg1|xargs sh ./pairs2.sh|xargs sh ./fib_seq2.sh >$arg2

