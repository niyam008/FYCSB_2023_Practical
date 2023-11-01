#!/bin/bash
a=5
# -gt is greater than operator
# print the loop untill a is greater than 10
until [$a -gt 15];
do
    # print the values
    echo $a
    # increment the value
    a=$(a+1)
done
