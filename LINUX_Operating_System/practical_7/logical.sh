#!/bin/bash
read -p "enter first number: " first
read -p "enter second number: " second
if [ $first -le 10 ] || [ $second -gt 20 ]
then
    echo "at least one condition is true"
else
    echo "both conditions are failed"
fi

