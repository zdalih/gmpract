''''
The parser creator for gmpract. This handles all
the logic, subparsers, and options that will
generate the args (parameters) that will run
the tool.

Author: Mohamed-Ali Hached
e-mail: mdali.hached@gmail.com
'''



import argparse

'''
Returns the arguments (parameters) as read by argparse

has the following subparsers:
	-SVM

the subparser used by the user is outlined by args.which, one
of the subparsers must be chosen else the parser will let the
user know of the possible positional arguments.

args is only returned if the parser finds that the user has
proivded arguments that satisfy what is outlined by the
setup of the parser and the subparser. else it will direct 
the user to a informative message printed on __stdout__
'''

def get_args():
	#THE PARSER ITSELF:

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

	#ADD ANY SUBPARSER FOR SUB-MODELS
	subparsers = parser.add_subparsers(help='Classififer Model')
	add_svm_subparser(subparsers)

	#GET THE ARGUMENTS
	args = parser.parse_args()

	#TODO make this more elegant
	#option: make gamma a class type
	#so that argparse understands that it's
	#default is a string and otherwise it's a float
	try:
		if args.gamma == None:
			args.gamma = 'auto'
	except AttributeError:
		pass

	return args

'''
Subparser for the SVM positional argument,
it parses the inputs that only apply to the SVM 
classifier model
'''
def add_svm_subparser(subparsers):
	svmParser = subparsers.add_parser('SVM',
		help = 'Use SVM Model.')
	svmParser.set_defaults(which='SVM')

	#the parameters for the SVM tool

	svmParser.add_argument('-run',
		required = True,
		action = 'store_true',
		help = 'Start the process.'
		)

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
