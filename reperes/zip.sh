#!/bin/bash

for TP in tp_2d tp_6axis tp_3axis tp_door
do
    rm -rf $TP/__pycache__
    zip -r $TP.zip ./$TP/
done

