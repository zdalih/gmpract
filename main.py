import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	#a random test argument to see if
	#docker image works and arguments
	#can be passed through it
	parser.add_argument(
		'-f',
		'--file',
		required = False,
		default = './test/test/',
		action='store',
		dest='input_file',
		help = 'Store file in db.')

	args = parser.parse_args()
	print(args)
