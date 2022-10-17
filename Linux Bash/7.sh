#!/bin/bash

ficheros=`ls *.txt`

for fichero in ficheros;
do
    mv -- "$fichero" "${fichero%.txt.sh"
done