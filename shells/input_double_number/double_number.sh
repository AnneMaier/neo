#!/bin/bash

read -p "Input number : " number

if [[ ! "$number" =~ ^[0-9]+$ ]]; then
	echo "Please enter number only."
	exit 1
fi

result=$((number * 2))

echo "Input number : $number"
echo "Double the entered number : $result"
