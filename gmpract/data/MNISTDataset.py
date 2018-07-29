from .Dataset import Dataset

import numpy as np

from tensorflow.examples.tutorials.mnist import input_data

class MNISTDataset(Dataset):
	'''
	the MNIST dataset as a subset of Dataset
	the reason for this architecture is that
	it makes it easy to add different datasets
	as long as the data structure of dataset 
	is the same.

	the following mnist import is credited to:
	Alexandre Drouin

	'''
	def __init__(self):
		mnist = input_data.read_data_sets("MNIST_data/", one_hot = False)

		x_train = np.vstack([img.reshape(-1,) for img in mnist.train.images])
		y_train = mnist.train.labels

		x_test = np.vstack([img.reshape(-1,) for img in mnist.test.images])
		y_test = mnist.test.labels

		Dataset.__init__(self, x_train, y_train, x_test, y_test)

