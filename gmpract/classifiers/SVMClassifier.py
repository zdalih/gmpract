import numpy as np

from sklearn.svm import SVC
from sklearn import metrics

class SVMClassifier():

	'''
	Initializes the SVM classifier.
	
	 PARAMETERS
	--------------------------------------------------------
	@param dataset: gmpract.data object 

	@param kernel_function: string - one of:
				-'linear'
				-'poly'
				-'rbf'
				-'sigmoid'

	@param loss_constant: float - the C constant in the sklearn SVM model

	@param rand_seed_param: int - the random seed parameter for sklearn SVM model
	
	@gamma - float, sets the gamma coefficient 
		- can either be a float or 'auto'
	
	@verbose - boolean, tells the classifier wether to print as it trains

	'''
	def __init__(self, **kwargs):
		#the dataset object has functions to give us training and testing sets
		self.dataset = kwargs['dataset']

		#initiate the classifer
		self.classifier = SVC(
			probability=False,
			kernel = kwargs.get('kernel_function'),
			C = kwargs.get('loss_constant'),
			random_state = kwargs.get('rand_seed_param'),
			gamma = kwargs.get('gamma'),
			verbose = kwargs.get('verbose')
			)

	'''
	Trains the classifier with the training data in self.dataset

	Takes no parameters.

	returns nothing prints nothing, unless the classifier was initialized
	with the verbose option, in which case sklearn will print iteration
	reports
	'''
	def train(self):
		self.classifier.fit(self.dataset.trainDataX(), self.dataset.trainDataY())

	'''
	The classifier must already have been trained or else it will raise an exception.

	It will return the accuracy of the classifier as tested on the dataset's 
	test data

	'''
	def accuracy(self):
		predictions = self.classifier.predict(self.dataset.testDataX())
		accuracy = metrics.accuracy_score(self.dataset.testDataY(), predictions)
		return accuracy
