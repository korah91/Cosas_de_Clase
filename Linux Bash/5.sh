#!/bin/bash
mkdir -p cosas
for (( i=0; i<100; i++ ))
do
    touch cosas/fich$i.txt
done