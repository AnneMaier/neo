#!/bin/bash

i=1
uid=$1
cnt=$2


while [ $i -le $cnt ]; do
    userdel -r user$1
    let uid+=1
    
done
echo "comelete delete"
!