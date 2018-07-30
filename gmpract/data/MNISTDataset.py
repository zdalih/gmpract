from .Dataset import Dataset

import numpy as np
import os, sys, contextlib

import tensorflow as tf
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

	@param num_datapoints between 0.01 and 1
		1 being all data points.
		and 0.01 being 1% of the dataset. 


	'''
	def __init__(self, size_scale = 1):
		#silence warnings
		tf.logging.set_verbosity(tf.logging.ERROR)

		#Stop tensorflow from printing
		#by temporarly changing stdout to None
		old_stdout = sys.stdout
		sys.stdout = None

		data_dir = os.path.join('/tmp/', 'MNIST_data')
		mnist = input_data.read_data_sets(data_dir, one_hot = False)

		#all the data points
		x_train = np.vstack([img.reshape(-1,) for img in mnist.train.images])
		y_train = mnist.train.labels

		x_test = np.vstack([img.reshape(-1,) for img in mnist.test.images])
		y_test = mnist.test.labels

		#scale the size of the dataset this is mostly for easy testing
		trainSize = int(len(x_train)*size_scale)
		testSize = int(len(x_test)*size_scale)

		x_train = x_train[0:trainSize]
		y_train = y_train[0:trainSize]

		#no need to change test length, because
		#it is snot computationally expensive, and it gives bad
		#accuracy readings if it changes every run	
		# x_test = x_test[0:testSize]
		# y_test = y_test[0:testSize]


		Dataset.__init__(self, x_train, y_train, x_test, y_test)

		del mnist
		sys.stdout = old_stdout
