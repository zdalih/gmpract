''''
gmpract command line tool to run and analyze the performance
of classifiers.

Author: Mohamed-Ali Hached
e-mail: mdali.hached@gmail.com
'''

import signal, sys

from gmpract.console.parser import get_args

def main():

	signal.signal(signal.SIGINT, exit_signal)
	signal.signal(signal.SIGTERM, exit_signal)

	try:
		#parse command inputs
		args = get_args()

		try: 
			
			args.which

		except AttributeError:
			print("Console tool to play with a SVM model on the MNIST dataset! \nEnter gmpract -h to see list of options.")
			shutdown()

		#execute the args
		print("Starting gmpract.")
		execute(args)

	except KeyboardInterrupt:
		print("SIGINT caught.")
		shutdown()


def execute(args):
	#import needed routines only when needed as to not
	#create any import lag
	from gmpract.console.routines import import_mnist
	mnistData = import_mnist(args)

	#based on args.which select what to do
	if args.which == 'SVM':
		from gmpract.console.routines import run_svm_classifier

		if args.verbose:
			run_svm_classifier(args, mnistData, spin = False)
		else:
			run_svm_classifier(args, mnistData)

def shutdown():
	sys.exit(0)
	

def exit_signal(signum, frame):
	raise KeyboardInterrupt

if __name__ == "__main__":
	main()

