#!/bin/bash

if [[ -d $1 ]]; then
    echo "It is a directory"
    cat $1 | more
elif [[ -f $1 ]]; then
    echo "It is a file"
fi
