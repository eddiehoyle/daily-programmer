/*
Challenge # 101
http://www.reddit.com/r/dailyprogrammer/comments/10l8ay/9272012_challenge_101_easy_nonrepeating_years/

This challenge comes to us from user skeeto[1] 
Write a program to count the number years in an inclusive range of years that have no repeated digits.
For example, 2012 has a repeated digit (2) while 2013 does not. Given the range [1980, 1987], your program would return 7 (1980, 1982, 1983, 1984, 1985, 1986, 1987).
Bonus: Compute the longest run of years of repeated digits and the longest run of years of non-repeated digits for [1000, 2013].
*/

function set(item){
		// Poor mans python set() with no checking
		list = item.toString().split("")
		data = []
		list.forEach(function(index){
			if (data.indexOf(index) == -1){
				data.push(index)
			}
		})
		return data
	}

function range(start, end){
	// Poor mans python range() with no checking
	list = [];
	while (start < end){
		list.push(start);
		start += 1;
	}
	return list
}

function recur(startNum, endNum, repeat){
	// Spose this should have a max recursion limit
	var repeat = repeat || false;
	var nums = []

	function inRecur(startNum, endNum, repeat){
		// Recursive method
		len = startNum.toString().split("").length
		if (repeat == true && set(startNum).length != len){
			nums.push(startNum);
			startNum += 1;
			if (startNum < endNum){
				inRecur(startNum, endNum, repeat);
			}
		}
		else if (repeat == false && set(startNum).length == len){
			nums.push(startNum)
			startNum += 1;
			if (startNum < endNum){
				inRecur(startNum, endNum, repeat);
			}
		}
		else{
			return nums
		}
	}

	inRecur(startNum, endNum, repeat)
	return nums
}


function getLongestRun(startNum, endNum, repeat){
	var repeat = repeat || false;
	var obj = {};
	var longest = 0;

	while (startNum < endNum) {
		numData = recur(startNum, endNum, repeat)
		
		// Store in obj object if found a num range
		if (numData.length > 1){
			
			// Generate unique object key
			index = 0;
			key = "range" + index;
			while (obj.hasOwnProperty(key)){
				index += 1;
				key = "range" + index
			}

			// Assign key to object with data
			obj[key] = {
				range: [numData[0], numData[numData.length-1]],
				items: numData
			}

			// Track the longest length of items
			if (obj[key].items.length > longest){
				longest = obj[key].items.length;
			}	
		}

		// Strip data to only be longest
		for (k in obj){
			if (obj[k].items.length < longest){
				delete obj[k]
			}
		}
		startNum += 1;
	}
	return obj
}
// ======================================================== //
// Run examples
// Currently this doesn't work for negative numbers. Or... years BC.

x = getLongestRun(1980, 1987, repeat=false)
for (k in x){
	debug(x[k].range + " - " + x[k].items)
}

x = getLongestRun(1000, 2013, repeat=true)
for (k in x){
	debug(x[k].range + " - " + x[k].items)
}

x = getLongestRun(1000, 2013, repeat=false)
for (k in x){
	debug(x[k].range + " - " + x[k].items)
}

