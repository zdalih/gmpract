import argparse

from gmpract.parser import add_svm_subparser, get_parser
from gmpract.data.MNISTDataset import MNISTDataset as mnist
from gmpract.classifiers.SVMClassifier import SVMClassifier as svm

def main():
	parser = get_parser()

	#add a subparser for each model supported
	subparsers = parser.add_subparsers(help='Classififer Model')
	add_svm_subparser(subparsers)

	#the args received
	args = parser.parse_args()
	
	#execute the args
	execute(args)


def execute(args):
	if args.which == 'SVM':
		mnistData = mnist()
		svmClassifier = svm(dataset = mnistData,
		kernel_function = args.kernel_function,
		loss_constant = args.loss_constant,
		rand_seed_param = args.rand_seed_param)

		svmClassifier.train()


if __name__ == "__main__":
	main()


# @contextmanager
# def suppress_stdout():
# 	with open(os.devnull, "w") as devnull:
# 		old_stdout = sys.old_stdout
# 		sys.stdout = devnull
# 		try:
# 			yield
# 		finally:
# 			sys.stdout = old_stdout
