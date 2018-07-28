#!/bin/bash

#pull the image
#docker pull gmpract

#copy executable script to bin
chmod +x ./gmpract.sh
cp ./gmpract.sh /bin/
#create alias
alias gmpract='sudo /bin/gmpract.sh'
echo 'Install complete, please try gmpract -h'