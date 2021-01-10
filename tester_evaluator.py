import random
random.seed(111)

with open("cases.txt", "r") as file:
	cases = [eval(i[:-1]) for i in file]


def get_data(): 	# This has the exact same function as the get_data() in evaluator.py.
	with open("DONOTTOUCH.txt", "r") as file:
		index = int(file.read())
	r = cases[index]
	index += 1
	with open("DONOTTOUCH.txt", "w") as file:
		file.write(str(index))
	return r
