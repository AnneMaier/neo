#!/bin/bash

config=$(ps -ef | grep 'mongoConifg')
router=$(ps -ef | grep 'mongoRouter')
shard1=$(ps -ef | grep 'mongoShard1')
shard2=$(ps -ef | grep 'mongoShard2')

secon1=$(echo ${config} | cut -d " " -f2)
secon2=$(echo ${router} | cut -d " " -f2)
secon3=$(echo ${shard1} | cut -d " " -f2)
secon4=$(echo ${shard2} | cut -d " " -f2)

for var in $second1 $second2 $second3 $second4
do
	echo $var
		if [ -n ${var} ]; then
			result=$(kill -9 ${var})
			echo process is killed.
		else
			echo running process not found.
		fi
done
echo
