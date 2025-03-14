#!/bin/bash

echo "File Name : $0 " #파일 명: 자기 자신
echo "Parameter Count : $# "
echo "All Parameter : $@ "

if [ "$1" = ok ]; then
    echo good~!!
else
    echo bad~!!
fi