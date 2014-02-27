'''
Challenge #100:
http://www.reddit.com/r/dailyprogrammer/comments/106go0/9202012_challenge_100_easy_sleep_cycle_estimator/

This challenge comes to us from nagasgura
	The human body goes through 90 minute sleep cycles during the night, 
	and you feel more refreshed if you wake up at the end of a sleep cycle 
	than if you wake up during a sleep cycle. The challenge is to make a program 
	that takes a wake-up time and outputs the possible times to fall asleep so 
	that you will wake up at the end of a sleep cycle.

Example:
	Input (Wake-up time): 6:15 AM
	Output (when to go to sleep): 9:15 PM, 10:45 PM, 12:15 AM, or 1:45 AM

Bonus 1: Be able to input a sleep time and output potential wake-up times
Bonus 2: Account for how long it takes to fall asleep
'''

from datetime import datetime, timedelta
import math

# How long each sleep cycle is in minutes
CYCLE = 90

# Get time to go to bed in order to wake up at input time 
def getBedTime(wakeUpTime, maxHours, minHours=0, fallAsleepOffset=0):
	
	# Lock down some variables
	if maxHours < 1.5:
		maxHours = 1.5
	if minHours < 1.5:
		minHours = 1.5
	if maxHours < minHours:
		maxHours = minHours
	
	# Create list of deltas that fit between 
	# min and max sleep time limits
	timeMax = timedelta(hours=maxHours)
	timeMin = timedelta(hours=math.ceil(minHours/1.5)*1.5)
	delta = timedelta(minutes=CYCLE)
	cycles =  []
	while delta <= timeMax:
		if delta < timeMin:
			delta += timedelta(minutes=CYCLE)
			continue

		cycles.append(delta)
		delta += timedelta(minutes=CYCLE)
	cycles.reverse()

	# Create times
	d = datetime.strptime(wakeUpTime, "%I:%M %p")
	bedTimes = []
	for i in cycles:
		t = (d-i-timedelta(minutes=fallAsleepOffset)) + timedelta(days=1)
		bedTimes.append(t.strftime("%I:%M %p"))

	return bedTimes

if __name__ == '__main__':

	# Input (Wake-up time): 6:15 AM
	# Output (when to go to sleep): 9:15 PM, 10:45 PM, 12:15 AM, or 1:45 AM
	print(getBedTime('6:15 AM', maxHours=9, minHours=4.5))

	# Bonus 1: Be able to input a sleep time and output potential wake-up times
	# Use fallAsleepOffset arg
	print(getBedTime('6:15 AM', maxHours=9, minHours=4.5, fallAsleepOffset=0))

	# Bonus 2: N/A

