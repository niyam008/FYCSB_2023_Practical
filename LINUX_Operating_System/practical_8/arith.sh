#!/bin/bash
# arithmetic
a=50
b=20
expr $a+$b
echo "a+b:$val"
expr $a-$b
echo "a-b:$val"
if [$a==$b]
then
    echo "a is equal to b"
fi
if [$a!=$b]
then
    echo "a is not equal to b"
fi
