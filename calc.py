from decimal import *
import math

def StrToMathList(str):
    mathList = []
    str += "@"
    operations = "+-/*()"
    value = ""

    for symbol in str:
        if symbol.isdigit():
            value += symbol
        elif symbol in operations:
            if value != "":
                mathList.append(value)
            mathList.append(symbol)
            value = ""
        elif symbol == "@":
            if value != "":
                mathList.append(value)
    return mathList

def MathListToPostfix(mathList):
    ExprData = []
    ExprOp = []
    prOp = {"+": 0, "-": 0, "*": 1, "/": 1, "(": 0, ")": 1}

    for item in mathList:
        if item.isdigit():
            ExprData.append(item)
        else: 
            if item in "()":
                if item == ")":
                    popOp = ExprOp[::-1].index("(")
                    for pop in range(0, popOp):
                        ExprData.append(ExprOp.pop())
                    ExprOp.pop()
            elif len(ExprOp) > 0 and (
                        prOp[item] < prOp[ExprOp[-1]] or 
                        item in "-/" and prOp[item] == prOp[ExprOp[-1]]):
                try:
                    popOp = ExprOp[::-1].index("(")
                except ValueError:
                    popOp = len(ExprOp)
                print popOp
                for pop in range(0, popOp):
                    ExprData.append(ExprOp.pop())
            if item != ")":
                ExprOp.append(item)
    return ExprData + ExprOp[::-1]

def evalute(stack):
    step = stack.pop()
    if step in "+-*/":
        var2 = evalute(stack)
        var1 = evalute(stack)
        if step == "+":
            return var1 + var2
        elif step == "-":
            return var1 - var2
        elif step == "*":
            return var1 * var2
        elif step == "/":
            return var1 / var2
        print step
    else:
        return Decimal(step)
        
def calculate(mathData):
    mathList = StrToMathList(mathData)
    postfix = MathListToPostfix(mathList)
    return evalute(postfix)



















