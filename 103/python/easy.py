#!/usr/bin/env python

'''
Back in the 90s (and early 00s) people thought it was a cool idea to \/\/|2][73 |_1|<3 7H15 to bypass text filters on BBSes. They called it Leet (or 1337)[1] , and it quickly became popular all over the internet. The habit has died out, but it's still quite interesting to see the various replacements people came up with when transforming characters.
Your job's to write a program that translates normal text into Leet, either by hardcoding a number of translations (e.g. A becomes either 4 or /-\, randomly) or allowing the user to specify a random translation table as an input file, like this:
A    4 /-\
B    |3 [3 8
C    ( {
(etc.)
Each line in the table contains a single character, followed by whitespace, followed by a space-separated list of possible replacements. Characters should have some non-zero chance of not being replaced at all.
'''

import random

table = {"A": ['/-\\', '/\\', '4', '@'],
         "B": ['|3', '8', '|o'],
         "C": ['(', '<'],
         "D": ['|)', ''],
         "E": ['3'],
         "F": ['|='],
         "G": ['9', '6'],
         "H": ['|-|', ']-[', '}-{', '#'],
         "I": ['1', '|', ']['],
         "J": ['_|'],
         "K": ['|<', '/<', '\\<', '|{'],
         "L": ['|_'],
         "M": ['|\\/|', '/\\/\\', "|'|'|", '/|\\'],
         "N": ['|\\|', '/\\/'],
         "O": ['0', '()'],
         "P": ['|`'],
         "Q": ['(,)'],
         "R": ['|2'],
         "S": ['5', '$'],
         "T": ['+', "']['", '7'],
         "U": ['|_|'],
         "V": ['\\/'],
         "W": ['\\/\\/', '|/\\|', '\\|/'],
         "X": ['><', '}{'],
         "Y": ['`/'],
         "Z": ['2']}


def translate(string):
    leet = ""
    try:
        for char in iter(string):

            # Determine result
            result = None

            # Space
            if char == " ":
                leet += " "*2
                continue

            char_array = table.get(char.upper(), [])
            if char_array:
                result = char_array[random.randint(0, (len(char_array)-1))]

            if not result:
                result = char

            # Add to string
            leet += result

        return leet

    except TypeError as e:
        return e

if __name__ == '__main__':
    print translate(324234)
