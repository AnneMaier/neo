#!/bin/bash

file1=$1
file2=$2


if [ $# -eq 2 ]; then
    if [ $file1 -nt $file2 ]; then
        echo "$file1 in newer than $file2."
    else
        echo "$file2 in newer than $file1."
    fi
else
    echo "Input Two parameters!"
fi