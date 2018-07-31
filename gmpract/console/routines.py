''''
Functions that are used by main.py , these are routines 
that achieves desired outcomes while printing to __stdout__
informative details.

Author: Mohamed-Ali Hached
e-mail: mdali.hached@gmail.com
'''


'''
Generate a MNISTDataset object while keeping track
of details on __stdout__

Parameters
___________

args - the argparser args with args.data_size_scale being a float
between 0.001 and 1 representing the share of the total training
dataset to user when creating the MNISTDataset object

returns a MNISTdataset object with training data of the size 
55,000*args.data_size_scale. 

prints to __stdout__ :
	Importing MNIST dataset
	Training Data Size = {Training set size}
	Testing Data Size = {Testing set size}
'''
def import_mnist(args):
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

	return mnistData



'''
Runs the svm classifier training and prints evaluation of performance. 

Parameters
__________

@args - argparse arg object as given by
	gmpract.console.parser with the SVM subparser
	parameters included.

@data - the MNISTDataset object with the training and
	testing dataset that will be used by the classifier

prints to __stdout__
	-Parameters used for the SVM classifier
	-Spinning Wheel
	-Time to Train
	-Accuracy

'''
def run_svm_classifier(args, data):
	from gmpract.classifiers.SVMClassifier import SVMClassifier as svm
	from gmpract.console.utilities import Spinner
	import time

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
