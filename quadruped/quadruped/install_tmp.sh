#!/bin/bash

if [ ! -d /tmp/py3 ]; then
	virtualenv --python=/usr/bin/python3 /tmp/py3
	source /tmp/py3/bin/activate
	pip3 install numpy scipy pybullet matplotlib
else
	source /tmp/py3/bin/activate
fi

