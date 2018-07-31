#!/bin/bash

#pull the docker image
docker pull zdalihach/gmpract:alpha

#copy executable script to bin
chmod +x ./gmpract
cp ./gmpract /bin/
#create alias
echo 'Install complete, please try gmpract -h'