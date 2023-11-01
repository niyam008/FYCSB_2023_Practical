#!/bin/bash
echo -n "Enter a number: "
read x
if [ $((x%2)) -eq 0 ]; then
    echo "The number is even."
else
    echo "The number is odd."
fi

