#!/usr/bin/env python

import re
import random
from os import path
from optparse import OptionParser

class LeetDict(dict):
    """
    """

    def __init__(self, _file, random_result=True):
        super(LeetDict, self).__init__()

        self.random_result = random_result
        self.__table = {}
        self.parse_file(_file)


    def get_table(self):
        return self.__table

    def get_leet_char(self, char):
        return self._get_char(char)

    def get_leet_row(self, char):
        return self._get_row(char)

    def translate(self, string):
        """
        """

        try:
            result = ""
            for char in iter(string):

                if char == " ":
                    result += " "
                    continue

                index = 0
                if self.random_result:
                    row = self._get_row(char)
                    index = random.randint(0, (len(row))-1)

                result += self._get_char(char, index)

            return result

        except Exception as e:
            self._log(e)

    def parse_file(self, _file):
        """
        """

        if not path.exists(_file):
            raise IOError("File does not exist")

        data = {}
        with open(_file) as f:
            for line in f.readlines():
                line_search = re.search("^([\w])\s+(.*)$", line)
                if line_search:
                    found = line_search.groups()
                    data[found[0]] = found[1].split()

        self.__table = data

    def _get_row(self, char):
        """
        Get row of leet characters
        """

        try:
            return self.__table[char.upper()]

        except KeyError(ke):
            self._log(ke)

    def _get_char(self, char, index):
        """
        """

        try:
            row = self._get_row(char.upper())
            return row[index]

        except KeyError as ke:
            self._log(ke)

        except IndexError as ie:
            self._log(ie)

    def _log(self, message):
        """
        """

        print message


















