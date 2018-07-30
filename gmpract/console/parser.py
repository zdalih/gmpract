import argparse

def get_parser():
	parser = argparse.ArgumentParser(description="""test accuracy of MNIST  
	classifiers with variable inputs.""")

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
	choices = [Range(0.001,1.0)],
	default = 1,
	action = 'store',
	dest = 'data_size_scale',
	help = 'Number between 0.001-1.0 referring the the percent of the MNIST database to train on.')

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


'''
Range class that can be passed in argparser
to specify the allowable range for float type 
'''
class Range:
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def __eq__(self, other):
		return self.start <= other <= self.end

	def __repr__(self):
		return ( 'Float Range : [%0.3f - %0.3f]' % (self.start, self.end) )

