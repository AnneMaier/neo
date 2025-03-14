#!/bin/bash

a=1

while [ "$a" != "0" ]; do
    echo -n "Input(0: exit) : "
    read a

    if [ "$a" -ge 2 -a "$a" -le 9 ]; then
        for ((k=1; k<=9; k++)); do
            echo "$a * $k = $((a * k))"
        done
    elif [ "$a" != "0" ]; then
        echo "Number must be 2~9"
    fi
done

echo "Exit"