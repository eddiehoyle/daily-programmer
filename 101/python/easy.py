'''
Challenge # 101
http://www.reddit.com/r/dailyprogrammer/comments/10l8ay/9272012_challenge_101_easy_nonrepeating_years/

This challenge comes to us from user skeeto[1] 
Write a program to count the number years in an inclusive range of years that have no repeated digits.
For example, 2012 has a repeated digit (2) while 2013 does not. Given the range [1980, 1987], your program would return 7 (1980, 1982, 1983, 1984, 1985, 1986, 1987).
Bonus: Compute the longest run of years of repeated digits and the longest run of years of non-repeated digits for [1000, 2013].
'''

def recur(y, repeat=False):
	'''
	Return list of years of repeating,
	or non-repeating digits
	'''
	data = []

	# Recursive function
	def inRecur(y, repeat):
		if repeat and len(set(list(str(y)))) != 4:
			data.append(y)
			y += 1
			inRecur(y, repeat)
		elif not repeat and len(set(list(str(y)))) == 4:
			data.append(y)
			y += 1
			inRecur(y, repeat)
		else:
			return data

	inRecur(y, repeat)

	return data

def getLongestRun(years, repeat=False):

	# Cycle through years
	data = {}
	longest = 0
	for y in range(years[0], years[1]+1):

		# Assign tuple year range as key and set 
		# item as repeat or no-repeat list
		
		yearRange = recur(y, repeat)
		if yearRange:
			key = (y, yearRange[-1])
			data[key] = yearRange

			if len(data[key]) > longest:
				longest = len(data[key])
		
		
	# Strip all data to be only longest
	for k in data.keys():
		if len(data[k]) < longest:
			del data[k]

	return data


if __name__ == '__main__':
	
	# First question of challenge
	noRepeat = getLongestRun([1980, 1987], repeat=False)
	print "Found %s range(s) of years with length of non-repeating numbers: %s" % (len(noRepeat.keys()), len(noRepeat[noRepeat.keys()[0]]))
	for key, item in noRepeat.iteritems():
		print "\t", key, item

	# Get longest range of repeating years
	repeat = getLongestRun([1000, 2013], repeat=True)
	print "Found %s range(s) of years with length of repeating numbers: %s" % (len(repeat.keys()), len(repeat[repeat.keys()[0]]))
	for key, item in repeat.iteritems():
		print "\t", key, item
	# Result:
	# Found 1 range(s) of years with length of repeating numbers: 104
	# 	(1099, 2013) [1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202]
	
	noRepeat = getLongestRun([1000, 2013], repeat=False)
	print "Found %s range(s) of years with length of non-repeating numbers: %s" % (len(noRepeat.keys()), len(noRepeat[noRepeat.keys()[0]]))
	for key, item in noRepeat.iteritems():
		print "\t", key, item
	# Result: 
	# Found 6 range(s) of years with length of repeating numbers: 7
	# 	(1234, 2013) [1234, 1235, 1236, 1237, 1238, 1239, 1240]
	# 	(1902, 2013) [1902, 1903, 1904, 1905, 1906, 1907, 1908]
	# 	(1092, 2013) [1092, 1093, 1094, 1095, 1096, 1097, 1098]
	# 	(1023, 2013) [1023, 1024, 1025, 1026, 1027, 1028, 1029]
	# 	(2013, 2013) [2013, 2014, 2015, 2016, 2017, 2018, 2019]
	# 	(1203, 2013) [1203, 1204, 1205, 1206, 1207, 1208, 1209]