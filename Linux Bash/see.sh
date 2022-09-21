#!/bin/bash

if [[ -d $1 ]]; then
    echo "It is a directory"
elif [[ -f $1 ]]; then
    echo "It is a file"
    cat $1 | more
fi
