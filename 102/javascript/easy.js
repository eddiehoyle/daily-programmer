/*
In tabletop role-playing games like Dungeons & Dragons, people use a system called dice notation[1] to represent a combination of dice to be rolled to generate a random number. Dice rolls are of the form AdB (+/-) C, and are calculated like this:
Generate A random numbers from 1 to B and add them together.
Add or subtract the modifier, C.
If A is omitted, its value is 1; if (+/-)C is omitted, step 2 is skipped. That is, "d8" is equivalent to "1d8+0".
Write a function that takes a string like "10d6-2" or "d20+7" and generates a random number using this syntax.

Here's a hint on how to parse the strings, if you get stuck:
Split the string over 'd' first; if the left part is empty, A = 1,
otherwise, read it as an integer and assign it to A. Then determine
whether or not the second part contains a '+' or '-', etc.

*/

function getRandomInt(min, max){
	// Get random int between min and max values
	return Math.floor(Math.random() * (max-min+1)) + min;
}


function roll(dice){

	// Dice regexp
	diceA = dice.match("^\\d+")
	diceB = dice.match("d(\\d+)")[1]
	op = dice.match("[-+?]")
	diceC = dice.match("\\d+$")

	// This captures everything, but bit tricky for me to work with
	// dice.match("(\\d+)d(\\d+)([-+?])(\\d+)").splice(1)

	// Collect dices values
	var values = new Array(3)
	if (diceA){
		values[0] = diceA
	}
	else{
		values[0] = 1
	}
	
	if (diceB){
		values[1] = diceB
	}
	else{
		values[1] = 1
	}

	if (diceC){
		if (op == "+"){
			values[2] = diceC
		}
		else{
			values[2] = -diceC
		}
	}
	else{
		values[2] = 0
	}

	// Compute roll
	min = Math.min.apply(Math, values.slice(0, 2))
	max = Math.max.apply(Math, values.slice(0, 2))
	return getRandomInt(min, max) - values[2]

}

// -------------------------------------------- //
// Use cases 
debug("Question input:")
debug(roll('10d6-2'))
debug(roll('d20+7'))

debug("Full input:")
debug(roll('5d2-1'))
debug(roll('12d7+5'))
debug(roll('5d8-8'))

debug("No dice A:")
debug(roll("d2+4"))
debug(roll("d6-2"))
debug(roll("d12+6"))

debug("No dice C:")
debug(roll("7d2"))
debug(roll("12d6"))
debug(roll("6d12"))
