#!/bin/bash


#pull the docker image
docker pull zdalihach/gmpract:gmpract-alpha

#copy executable script to bin
chmod +x ./gmpract.sh
rm /bin/gmpract.sh
cp ./gmpract.sh /bin/
#create alias
alias gmpract='sudo /bin/gmpract.sh'
echo 'Install complete, please try gmpract -h'