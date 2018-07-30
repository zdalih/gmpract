import argparse

def get_parser():
	parser = argparse.ArgumentParser(description="""test accuracy of MNIST  
	classifiers with variable inputs.""")
	svm.set_defaults(which=None)

	#verbose mode
	parser.add_argument('-v',
	'--verbose',
	required = False,
	default = False,
	action = 'store_true',
	dest = 'verbose',
	help = 'Allow all modules to print to stdout')

	#verbose mode
	parser.add_argument('-d',
	'--datasize',
	required = False,
	type = float,
	default = 1,
	action = 'store',
	dest = 'data_size_scale',
	help = 'Number between 0-1 referring the the percent of the MNIST database to train on.')

	#add a subparser for each model supported
	subparsers = parser.add_subparsers(help='Classififer Model')
	add_svm_subparser(subparsers)

	return parser

def add_svm_subparser(subparsers):
	svmParser = subparsers.add_parser('SVM',
		help = 'Use SVM Model.')
	svmParser.set_defaults(which='SVM')

	#the following are required params
	#type as per sklearn documentation

	svmParser.add_argument('-k',
		'--kernelfunc',
		required = True,
		choices = ['linear', 'poly', 'rbf', 'sigmoid'],
		action = 'store',
		dest = 'kernel_function',
		help = 'Choose one of the SVM kernel functions.')

	svmParser.add_argument('-c',
		'--penalconst',
		required = True,
		type = float,
		action = 'store',
		dest = 'loss_constant',
		help = 'Set the penalty "C" constant.')

	svmParser.add_argument('-s',
		'--randseedparam',
		required = True,
		type = int,
		action = 'store',
		dest = 'rand_seed_param',
		help = 'Set the random seed parameter')