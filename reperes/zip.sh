#!/bin/bash

for TP in tp_2d tp_6axis
do
    rm -rf $TP/__pycache__
    zip -r $TP.zip ./$TP/
done

