# gmpract
Command line tool that takes SVM kernel, penalty constant, and random seed parameters as inputs and returns the model accuracy as output using the MNIST dataset.

# Installation

## Option 1 : Docker Image [Recomended]

Requirements:
*Docker Installed
*Linux Distribution

If you do not have Docker installed you can either follow Docker's instruction for your distribution: https://docs.docker.com/install/#general-availability. Or use the following install script:

```
sudo apt-get install curl 

curl -fsSL get.docker.com -o get-docker.sh
sh get-docker.sh
```

With docker installed, use git to clone the repo and move into the gmpract/bin folder.

```
sudo apt-get install git
git clone https://github.ubc.ca/dalihach/gmpract.git
cd gmpract/bin
```

Now run the install script.

```
sudo sh ./install.sh
alias gmpract='sudo /bin/gmpract.sh'
```

Try ```gmpract -h```, if you get a help message you are good to go.

## Option 2 : Use Python Script [Faster]

Requirements:
*Python >= 3.5
*Linux Distribution

Ensure Python >= 3.5 and git is installed on your machine. 

```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install git
```

Clone the repo and move into the directory:


```
git clone https://github.ubc.ca/dalihach/gmpract.git
cd gmpract
```

Install requirements with pip3:

```
pip3 install -r requirements.txt
```

You are now in a position to run ```python3 main.py -h``` to see if you can succesfully print the help message. For a more user friendly experience you can set an alias:

```
alias gmpract=$'python3 '$(pwd)$'/main.py'
```
