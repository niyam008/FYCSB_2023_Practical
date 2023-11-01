#!/bin/bash
#redirect file input
exec < file1.txt
count=1
while read line
do
    echo "line #$count: $line"
    count=$[ $count +1 ]
done
