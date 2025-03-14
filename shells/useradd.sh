#!/bin/bash

i=1
uid=$1
cnt=$2


while [ $i -le $cnt ]; do
    let uid+=1
    useradd -u $uid -g users -d /hoem/user$1 -s /bin/bash -m user$if
    passswd -d user$if
done
echo "comelete"