from decimal import *
import math

getcontext().prec = 6

Err = {
    "ErrZeroDiv": "Sorry. I can't divide by zero :( Really",
    "ErrBracket": "Sorry. I can't evalute because count of brackets is amazing!!!",
    "ErrChar": "Sorry. I can't understand some characters :(",
    "ErrOps": "Sorry. I can't understand what you want exactly :(",
    "ErrNum": "Sorry. You give me very interesting numbers. I don't know how to identify them :(",
}

def strToMathList(str):
    mathList = []
    str += "@"
    operations = "+-/*"
    brackets = "()"
    value = ""
    lastOpFlag = True
    floatFlag = False

    for symbol in str:
        if symbol.isdigit() or symbol == "-" and value == "" and ( len(mathList)==0 or len(mathList)>0 and mathList[-1] in "("):
            value += symbol
        elif symbol == ".":
            if not floatFlag:
                value += symbol
                floatFlag = True
            else:
                return Err["ErrNum"]
        elif symbol in operations:
            if len(mathList)>0 and mathList[-1] in operations and value == "" or len(mathList) == 0 and value == "":
                return Err["ErrOps"]
            else:
                if value != "":
                    mathList.append(value)
                mathList.append(symbol)
                lastOpFlag = True
                floatFlag = False
                value = ""
        elif symbol in brackets:
            if symbol == "(" and not lastOpFlag or symbol == "(" and value != "":
                return Err["ErrOps"]
            if symbol == ")" and lastOpFlag and value == "":
                return Err["ErrOps"]
            elif value != "":
                mathList.append(value)
                lastOpFlag = False
            mathList.append(symbol)
            value = ""
        elif symbol == " ":
            if value != "" and lastOpFlag:
                mathList.append(value)
                value = ""
                lastOpFlag = False
                floatFlag = False
            elif value != "" and not lastOpFlag:
                return Err["ErrOps"]
            else:
                pass
        elif symbol == "@":
            if value != "" and lastOpFlag:
                mathList.append(value)
            elif value == "":
                pass
            else:
                return Err["ErrOps"]
        else:
            return Err["ErrChar"]

    lastElem = "@"
    brackets = 0
    for item in mathList:
        if item == "(":
            brackets += 1
        elif item == ")":
            brackets -= 1
        if brackets < 0:
            return Err["ErrBracket"]
        # if item in not operations and lastElem in operations: #or item not in operations and lastElem not in operations:
        # if item == "(" and lastElem != "@" and v:
            return Err["ErrOps"]
        lastElem = item
    if brackets != 0:
        return Err["ErrBracket"]

    return mathList

def mathListToPostfix(mathList):
    ExprData = []
    ExprOp = []
    prOp = {"+": 0, "-": 0, "*": 1, "/": 1, "(": 0, ")": 1}

    for item in mathList:
        isDigit = False
        try:
            float(item)
            isDigit = True
        except ValueError:
            isDigit = False

        if isDigit:
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
                for pop in range(0, popOp):
                    ExprData.append(ExprOp.pop())
            if item != ")":
                ExprOp.append(item)
    return ExprData + ExprOp[::-1]

def opSum(a, b):
    return a + b

def opSub(a, b):
    return Decimal(a) - Decimal(b)

def opMult(a, b):
    return Decimal(a) * Decimal(b)

def opDiv(a, b):
    if b != 0:
        return Decimal(a) / Decimal(b)
    else:
        return Err["ErrZeroDiv"]

operations= {
    "+": opSum,
    "-": opSub,
    "*": opMult,
    "/": opDiv
}

def evalute(stack):
    step = stack.pop()
    if step in "+-*/":
        var2 = evalute(stack)
        var1 = evalute(stack)
        result = operations[step](var1, var2)
        if result in Err.values():
            return result
        else:
            return Decimal(result)
    else:
        return Decimal(step)
        
def calculate(mathData):
    mathList = strToMathList(mathData)

    if mathList in Err.values():
        return mathList
    else:
        postfix = mathListToPostfix(mathList)

    result = evalute(postfix)

    if result in Err.values():
            return result
    elif result % 1 == 0:
        return int(result)
    else:
        return float(result)
