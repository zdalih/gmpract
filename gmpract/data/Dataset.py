class Dataset:
	'''
	dataset object has two tuples.

	train - (x_train,y_train) 
		x,y being numpy arrays for the
		training data and labels

	test - (x_test,y_test)
		same as the train tuple

	it has functions to get train/test
	data and labels arrays

	x is data itself while y is label

	TODO: be more specific about the nature
	of the arrays. 
	'''
	def __init__(self, x_train, y_train, x_test, y_test):
		self.train = (x_train, y_train)
		self.test = (x_test, y_test)

	def trainDataX(self):
		return self.train[0]

	def trainDataY(self):
		return self.train[1]

	def testDataX(self):
		return self.test[0]

	def testDataY(self):
		return self.test[1]


