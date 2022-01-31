#!/bin/bash

for TP in tp_*
do
    if [ -d $TP ]; then
        rm -rf $TP/__pycache__
        zip -r $TP.zip ./$TP/
    fi
done

