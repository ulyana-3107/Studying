#!/bin/bash

c1=0
c2=0
for elem in "$@"
do
        c1=$(($c1 + 1))
        c2=$(($c2 + 1))
        if [ $c1 -eq "$#" ]
        then
                if [ $c2 -eq 2 ]
                then
                        b=$elem
                        if [ $a -ge $b ]
                        then
                                param=$a
                        elif [ $b -ge $a ]
                        then
                                param=$b
                        fi
                        if [ $param -lt 0 ]
                        then
                                par=$(($param*$param))
                                echo $par
                        elif [ $param -ge 0 ]
                        then echo $param
                        fi
                        echo #####################
                elif [ $c2 -eq 1 ]
                then
                        a=$elem
                        b=0
                        if [ $a -ge $b ]
                        then
                                param=$a
                        elif [ $b -ge $a ]
                        then
                                param=$b
                        fi
                        if [ $param -lt 0 ]
                        then
                                par=$(($param * $param))
                                echo $par
                        elif [ $param -ge 0 ]
                        then
                                echo $param
                        fi
                        echo #####################
                fi
        elif [ $c1 -lt "$#" ]
        then
                if [ $c2 -eq 1 ]
                then
                        a=$elem
                elif [ $c2 -eq 2 ]
                then
                        b=$elem
                        if [ $a -ge $b ]
                        then
                                param=$a
                        elif [ $b -ge $a ]
                        then
                                param=$b
                        fi
                        if [ $param -lt 0 ]
                        then
                                par=$(($param * $param))
                                echo $par
                        elif [ $param -ge 0 ]
                        then
                                echo $param
                        fi
                        c2=0
                        echo #####################
                fi
        fi



done
