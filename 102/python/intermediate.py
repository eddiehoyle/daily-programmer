'''
Write a function that takes a string s and an integer n, and returns whether or not the string s contains at most n different characters.
'''

import time

WORDS_FILE = "/Users/eddiehoyle/Sites/dailyProgrammer/enable1.txt"

def ncset(string, num):
	'''Determines if string contains at most num characters'''
	return len(set(string)) <= num


# More information on this:
# http://stackoverflow.com/questions/5478351/python-time-measure-function
def timing(f):
	def wrap(*args):
		time1 = time.time()
		ret = f(*args)
		time2 = time.time()
		print "%s function took %s0.3f ms" % (f.func_name, (time2-time1)*1000.0)
		return ret
	return wrap

@timing
def question():
	strings = []
	num = 4
	with open(WORDS_FILE) as f:
		for l in f.readlines():
			clean = l.strip()
			if ncset(clean, num):
				strings.append(clean)

	return "Found %s words with at most %i character(s)." % (len(strings), num)


if __name__ == "__main__":
	print question()