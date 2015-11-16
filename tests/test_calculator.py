# -*- coding: utf-8 -*-

import unittest
from calc import *


class CalculatorTestCase(unittest.TestCase):

	def testSum1(self):
		self.assertEquals(calculate("1+1"), 2)

	def testSub1(self):
		self.assertEquals(calculate("5-4"), 1)

	def testMult1(self):
		self.assertEquals(calculate("6*8"), 48)

	def testDiv1(self):
		self.assertEquals(calculate("15/5"), 3)

	def testSpaces(self):
		self.assertEquals(calculate("8 + 6 "), 14)

	def testSum2(self):
		self.assertEquals(calculate("1+1+4"), 6)

	def testSub2(self):
		self.assertEquals(calculate("15-4-2"), 9)

	def testMult2(self):
		self.assertEquals(calculate("5*3*5"), 75)

	def testDiv2(self):
		self.assertEquals(calculate("24/6/2"), 2)

	def testBrackets1(self):
		self.assertEquals(calculate("(1+4)*3"), 15)

	def testBrackets2(self):
		self.assertEquals(calculate("(1+4)*(5+6)"), 55)

	def testBrackets3(self):
		self.assertEquals(calculate("25/5 + (4+8)/6 + (70/10-3)*5"), 27)


