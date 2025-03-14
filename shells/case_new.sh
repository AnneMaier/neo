#!/bin/bash

empty=""

if [ $# -eq 0 ]; then
    echo "Enter the Country Name!";
else

    case "$1" in
        ko) echo "Seoul";;
        us) echo "Washington";;
        cn) echo "Beijing";;
        jp) echo "Tokyo";;
        $empty) echo "You typed nothing";;
        *) echo "Your Entry => $1 is not in the list";;
    esac
fi