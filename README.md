# gmpract
Command line tool that takes SVM kernel, penalty constant, and random seed parameters as inputs and returns the model accuracy as output using the MNIST dataset.

# Installation

## Option 1 : Docker Image [Recomended]

Requirements:
* Docker Installed
* Linux Distribution

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
```

Try ```gmpract -h```, if you get a help message you are good to go.

## Option 2 : Use Python Script [Faster]

Requirements:
* Python >= 3.5
* Linux Distribution

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

try gmpract -h, if the help prompt prints out you are good!

# Usage

The gmpract tool allows one to use the MNIST dataset to train a chosen classifier model and evaluate it's accuracy and training time. 

#### -d [PORTION_DATASET] - Scale the size of the training dataset. A float between 0.001 and 1. [default = 1]

One can choose the percent of the MNIST training dataset to use (55,000 training images) in order to circumvent the long training times. The -d option set's the training data scale parameter, it is the percent of the total data to use for training.

Example - run default SVM model with half of the mnist dataset
```
gmpract -d 0.5 SVM -run
```

#### -v, --verbose - Sets verbose if option is present.

Allows sklearn module to print while it is training.

Examle - run default SVM model with all of the mnist dataset, while verbose.

```
gmpract -v SVM -run
```

#### -h, --help - Prints help prompt

Prints help prompt for the current parser.

Exemple: will print the available options for the tools
```
gmpract -h
```

### Model: Support Vector Machine {SVM}

Selects the SVM model for training. Implemented using sklearn SVC's module. To print the SVM classifier sub-process's help:

```
gmpract SVM -h
```

### -run - Tells us to run the SVM classifier. REQUIRED!

Must be set to run the tool.

#### -k, --kernel [KERNEL_FUNCTION] - Choose one of the kernel functions [default = linear]

Choices are: {linear, rbf, poly, sigmoid}

#### -c, --penalconstant [LOSS_PENALTY_CONSTANT] - Set the C constant - a float [default = 1]

Any float.

#### -s, --randseedparam [SEED] - The seed for the random generator - int [default = None]

The default value is None meaning the model will not be using the random generator. 

#### -g, --gamma - Set gamma [GAMMA] - float [default = auto]

If not set, it will be auto or 1/n where n is the training size. 

#### -h, --help - Print help prompt

---------------

Example to use the SVM model with 10% of the MNIST dataset. Setting the loss penalty constant to 1e6, using the rbf kernel function, allowing gamma to be auto, and seeting the random seed parameter to 1:

```
gmpract -d 0.1 SVM -run --kernel rbf -c 1e6 -s 0
```
