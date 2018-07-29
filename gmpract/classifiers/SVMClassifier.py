import numpy as np

from sklearn.svm import SVC


class SVMClassifier():

	'''
	Initializes the SVM classifier.
	
	REQUIRED PARAMETERS
	--------------------------------------------------------
	@param dataset: gmpract.data object 

	@param kernel_function: string - one of:
				-'linear'
				-'poly'
				-'rbf'
				-'sigmoid'

	@param loss_constant: float - the C constant in the sklearn SVM model

	@param rand_seed_param: int - the random seed parameter for sklearn SVM model
	
	OPTIONAL PARAMETERS
	-----------------------------------------------------
	@gamma - float, sets the gamma coefficient 
		- default is auto (1/n)

	throws KeyError

	'''
	def __init__(self, **kwargs):
		#the dataset object has functions to give us training and testing sets
		self.dataset = kwargs['dataset']

		#initiate the classifer
		self.classifier = SVC(probability=False,
			kernel = kwargs.get('kernel_function'),
			C = kwargs.get('loss_constant'),
			random_state = kwargs.get('rand_seed_param'),
			gamma = kwargs.get('gamma','auto'),
			verbose = 3
			)

	'''
	Trains the classifier with the training data in self.dataset

	Takes no parameters.

	returns nothing prints nothing
	'''
	def train(self):
		self.classifier.fit(self.dataset.trainDataX(), self.dataset.trainDataY())