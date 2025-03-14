#!/bin/bash

a=0

echo -n "Input : "
read a
let a/=10

case $a in
    10) echo A+;;
    9) echo A;;
    8) echo B;;
    7) ehco C;;
    6) echo D;;
    *) echo F.. Your Loser.;;

esac
echo "Thank you!"