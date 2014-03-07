'''
In tabletop role-playing games like Dungeons & Dragons, people use a system called dice notation[1] to represent a combination of dice to be rolled to generate a random number. Dice rolls are of the form AdB (+/-) C, and are calculated like this:
Generate A random numbers from 1 to B and add them together.
Add or subtract the modifier, C.
If A is omitted, its value is 1; if (+/-)C is omitted, step 2 is skipped. That is, "d8" is equivalent to "1d8+0".
Write a function that takes a string like "10d6-2" or "d20+7" and generates a random number using this syntax.

Here's a hint on how to parse the strings, if you get stuck:
Split the string over 'd' first; if the left part is empty, A = 1,
otherwise, read it as an integer and assign it to A. Then determine
whether or not the second part contains a '+' or '-', etc.

'''

import re, random, operator

def roll(dice):

	# Get re data
	diceA = re.search(r'^\d+', dice) # If string begins with number, find it
	diceB = re.search(r'\B(\d+)', dice) # Find number between two non word characters (d, operator)
	op = re.search(r'^\W', dice) # Find non-alphanumeric character
	diceC = re.search(r'[\d+]$', dice) # Find last number in string

	values = []

	# This is messy. Research this!
	# Dice A
	if diceA:
		values.append(int(diceA.group()))
	else:
		values.append(1)

	# Dice B
	values.append(int(diceB.group()))

	# Op
	if op:
		values.append(op.group())
	else:
		values.append('+') # Default operator

	# Dice C
	if diceC:
		values.append(int(diceC.group()))
	else:
		values.append(0)
	
	r = random.randint(int(min(values[0], values[1])), int(max(values[0], values[1])))
	ops = { "+": operator.add, "-": operator.sub }

	return ops[values[2]](r, values[3])


if __name__ == '__main__':
	print "Question input:"
	print roll('10d6-2')
	print roll('d20+7')
	
	print "Full input:"
	print roll('5d2-1')
	print roll('12d7+5')
	print roll('5d8-8')

	print "No dice A:"
	print roll("d2+4")
	print roll("d6-2")
	print roll("d12+6")

	print "No dice C:"
	print roll("7d2")
	print roll("12d6")
	print roll("6d12")
