#!/bin/bash

for i in {1..4}
do 
mynum=$(($RANDOM % 98000))
awk 'NR=='$mynum /usr/share/dict/usa
done
