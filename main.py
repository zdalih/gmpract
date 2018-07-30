import argparse
import signal, sys, io
import time

from gmpract.console.parser import add_svm_subparser, get_parser
from gmpract.console.utilities import Spinner

def main():

	signal.signal(signal.SIGTERM, exit_signal)
	signal.signal(signal.SIGINT, exit_signal)

	try:

		#parse command inputs
		parser = get_parser()
		args = parser.parse_args()

		#execute the args
		execute(args)

	except SystemExit:
		print("SIGINT caught.")
		shutdown()


def execute(args):
	#why import here? because it is not efficient to
	#import these before the parser has 
	#taken appropriate inputs.
	from gmpract.data.MNISTDataset import MNISTDataset as mnist
	from gmpract.classifiers.SVMClassifier import SVMClassifier as svm

	if args.which == 'SVM':
		mnistData = mnist(size_scale = args.data_size_scale)
		trainSize = len(mnistData.trainDataX())
		testSize = len(mnistData.testDataX())
		print("Training Data Size  = " + str(trainSize))
		print("Testing Data Size = " + str(testSize))


		svmClassifier = svm(dataset = mnistData,
		kernel_function = args.kernel_function,
		loss_constant = args.loss_constant,
		rand_seed_param = args.rand_seed_param,
		verbose = args.verbose)
		# rand_seed_param = args.rand_seed_param)

		#get the spinner going
		print("""\nSVM model with:
			Kernel Function = %s
			Loss Constant = %f 
			Random Seed Parameter = %i \n""" 
			%(args.kernel_function, args.loss_constant, args.rand_seed_param))

		print("Training model - please be patient!")
		spinner = Spinner()
		spinner.start()

		t = time.time()
		svmClassifier.train()
		elapsed = time.time() - t

		spinner.stop()

		accuracy = svmClassifier.accuracy()

		print("\nTraining took %0.2f seconds" % elapsed)
		print("Accuracy: %0.4f" % accuracy)



def shutdown():
	print("Shuting down...")
	sys.exit(0)
	

def exit_signal(signum, frame):
	raise SystemExit

if __name__ == "__main__":
	main()

