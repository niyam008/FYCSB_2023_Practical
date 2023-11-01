#!/bin/bash
echo -n "enter number"
read x
if [$(x%2)==0];then
    echo 'number is even'
else
    echo 'number is odd
    fi
