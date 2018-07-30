import argparse
import signal, sys
import time

from gmpract.console.parser import get_args
from gmpract.console.utilities import Spinner

def main():

	signal.signal(signal.SIGINT, exit_signal)

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
	#import here so that we only import once we have proper inputs
	#which makes its more efficient
	from gmpract.data.MNISTDataset import MNISTDataset as mnist

	#get MNIST data readydata ready
	print('Importing MNIST dataset.')
	mnistData = mnist(size_scale = args.data_size_scale)
	#information about the training and test data sizes
	trainSize = len(mnistData.trainDataX())
	testSize = len(mnistData.testDataX())
	print("Training Data Size  = " + str(trainSize))
	print("Testing Data Size = " + str(testSize))

	#based on args.which select what to do
	if args.which == 'SVM':
		run_svm_classifier(args, mnistData)

'''
Runs the svm classifier training and
evaluation of performance. 

Parameters
__________

@args - argparse arg object as given by
		gmpract.console.parser Must be as outlined
		by the arguments of the parser

prints to the console
	-parameters passed
	-time to train
	-accuracy

'''
def run_svm_classifier(args, data):
	from gmpract.classifiers.SVMClassifier import SVMClassifier as svm

	svmClassifier = svm(dataset = data,
	kernel_function = args.kernel_function,
	loss_constant = args.loss_constant,
	rand_seed_param = args.rand_seed_param,
	gamma = args.gamma,
	verbose = args.verbose)

	
	print("""\nSVM model with:
		Kernel Function = %s
		Loss Constant = %f 
		Random Seed Parameter = %s
		Gamma = %s \n""" 
		%(args.kernel_function, args.loss_constant, args.rand_seed_param, args.gamma))

	print("Training model - may take a while!")

	#get the spinner going on terminal
	spinner = Spinner()
	spinner.start()

	t = time.time()
	#train the model
	svmClassifier.train()
	elapsed = time.time() - t

	spinner.stop()
	del spinner

	accuracy = svmClassifier.accuracy()

	print("\nTraining took %0.2f seconds" % elapsed)
	print("Accuracy: %0.4f" % accuracy)

def shutdown():
	sys.exit(0)
	

def exit_signal(signum, frame):
	raise KeyboardInterrupt

if __name__ == "__main__":
	main()

