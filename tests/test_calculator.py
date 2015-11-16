# -*- coding: utf-8 -*-

import unittest
from calc import *


class CalculatorTestCase(unittest.TestCase):

	# Positive Tests

	def testSumSimpleInt(self):
		self.assertEquals(calculate("45+78"), 123)

	def testSubSimpleInt(self):
		self.assertEquals(calculate("15-85"), -70)

	def testMultSimpleInt(self):
		self.assertEquals(calculate("6*8"), 48)

	def testDivSimpleInt(self):
		self.assertEquals(calculate("15/5"), 3)

	def testSumSimpleFloat(self):
		self.assertEquals(calculate("0.2+0.1"), 0.3)

	def testSubSimpleFloat(self):
		self.assertEquals(calculate("2.3-1.1"), 1.2)

	def testMultSumpleFloat(self):
		self.assertEquals(calculate("12*0.1"), 1.2)

	def testDivSimpleFloat(self):
		self.assertEquals(calculate("4/1.1"), 3.63636)

	def testFloatZero(self):
		self.assertEquals(calculate("0.1+0.2-0.1-0.2"), 0)

	def testFloatWithZero(self):
		self.assertEquals(calculate(".4 - .0004"), 0.3996)

	def testStringWithSpaces(self):
		self.assertEquals(calculate("    8    +   6   "), 14)

	def testNegativeInt(self):
		self.assertEquals(calculate("-20+11"), -9)

	def testNegativeFloat(self):
		self.assertEquals(calculate("-0.009*63.4"), -0.5706)

	def testSumSeq(self):
		self.assertEquals(calculate("1+1+4"), 6)

	def testSubSeq(self):
		self.assertEquals(calculate("15-4-2"), 9)

	def testMultSeq(self):
		self.assertEquals(calculate("5*3.2*5"), 80)

	def testDivSeq(self):
		self.assertEquals(calculate("24/6/2"), 2)

	def testBracketsSimple(self):
		self.assertEquals(calculate("(1+4)*3"), 15)

	def testBracketsSeq(self):
		self.assertEquals(calculate("(1+4)*(5+6)"), 55)

	def testBracketsRepeat(self):
		self.assertEquals(calculate("((((1+2))))"), 3)

	def testBracketsAttach(self):
		self.assertEquals(calculate("(1+(2+3+(3+4)))"), 13)

	def testBracketsMix(self):
		self.assertEquals(calculate("25/5 + (4+8)/6 + (70/10-3)*5"), 27)

	def testIntResult(self):
		self.assertAlmostEquals(calculate("1.5/.5"), 3)

	# Negative Tests
	def testDivZero(self):
		self.assertEquals(calculate("1/0"), Err["ErrZeroDiv"])

	def testWrongChars(self):
		self.assertEquals(calculate("a+b"), Err["ErrChar"])

	def testWrongBracketOpen(self):
		self.assertEquals(calculate("((1+2)*6+1"), Err["ErrBracket"])

	def testWrongBracketClose(self):
		self.assertEquals(calculate("(1+2))*6+1"), Err["ErrBracket"])

	def testWrongSeqOps(self):
		self.assertEquals(calculate("12+*5"), Err["ErrOps"])

	def testWrongOperands(self):
		self.assertEquals(calculate("*5+1"), Err["ErrOps"])

	def testNoOpsWithSpace(self):
		self.assertEquals(calculate("23 777"), Err["ErrOps"])

	def testNoOpsWithOpenBrack(self):
		self.assertEquals(calculate("23(777)"), Err["ErrOps"])

	def testNoOpsWithCloseBrack(self):
		self.assertEquals(calculate("2*(77+)"), Err["ErrOps"])

	def testDoublePoints(self):
		self.assertEquals(calculate("1.2.3 + 4"), Err["ErrNum"])

	def testPointWithSpace(self):
		self.assertEquals(calculate("1 . 4"), Err["ErrOps"])

	# ((((1+2))))
	# (1+(2+3+(3+4)))