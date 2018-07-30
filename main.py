import argparse
import signal, sys
import time

from gmpract.console.parser import get_parser
from gmpract.console.utilities import Spinner

def main():

	signal.signal(signal.SIGINT, exit_signal)

	try:

		#parse command inputs
		parser = get_parser()
		args = parser.parse_args()

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
	from gmpract.classifiers.SVMClassifier import SVMClassifier as svm

	print('Importing MNIST dataset.')
	mnistData = mnist(size_scale = args.data_size_scale)
	trainSize = len(mnistData.trainDataX())
	testSize = len(mnistData.testDataX())
	print("Training Data Size  = " + str(trainSize))
	print("Testing Data Size = " + str(testSize))

	if args.which == 'SVM':

		svmClassifier = svm(dataset = mnistData,
		kernel_function = args.kernel_function,
		loss_constant = args.loss_constant,
		rand_seed_param = args.rand_seed_param,
		verbose = args.verbose)

		
		print("""\nSVM model with:
			Kernel Function = %s
			Loss Constant = %f 
			Random Seed Parameter = %i \n""" 
			%(args.kernel_function, args.loss_constant, args.rand_seed_param))

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

