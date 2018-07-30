import argparse

def get_args():
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

	args = parser.parse_args()

	#TODO make this more elegant
	#option: make gamma a class type
	#so that argparse understands that it's
	#default is a string and otherwise it's a float
	if args.gamma == None:
		args.gamma = 'auto'

	return args

def add_svm_subparser(subparsers):
	svmParser = subparsers.add_parser('SVM',
		help = 'Use SVM Model.')
	svmParser.set_defaults(which='SVM')

	#the following are required params
	#type as per sklearn documentation

	svmParser.add_argument('-k',
		'--kernelfunc',
		required = False,
		default = 'linear',
		choices = ['linear', 'poly', 'rbf', 'sigmoid'],
		action = 'store',
		dest = 'kernel_function',
		help = 'Choose one of the SVM kernel functions. [default = linear]')

	svmParser.add_argument('-c',
		'--penalconst',
		required = False,
		default = 1,
		type = float,
		action = 'store',
		dest = 'loss_constant',
		help = 'Set the penalty "C" constant. [default = 1]')

	svmParser.add_argument('-s',
		'--randseedparam',
		required = False,
		type = int,
		action = 'store',
		dest = 'rand_seed_param',
		help = 'Set the random seed parameter [default = None]')

	svmParser.add_argument('-g',
		'--gamma',
		required = False,
		type = float,
		action = 'store',
		dest = 'gamma',
		help = 'Set the gamma constant. [default = auto]')


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
