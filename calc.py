from decimal import Decimal, getcontext
import math

getcontext().prec = 6

Err = {
    "ErrZeroDiv": "Sorry. I can't divide by zero :( Really",
    "ErrBracket": "Sorry. I can't evalute because count of brackets is amazing!!!",
    "ErrChar": "Sorry. I can't understand some characters :(",
    "ErrOps": "Sorry. I can't understand what you want exactly :(",
    "ErrNum": "Sorry. You give me very interesting numbers. I don't know how to identify them :(",
    "ErrLog": "Ok, You have to use log(a,b) where a > 0 and b != 1 and b > 0",
}

def checkLogRight(mathList):
    posL = len(mathList) - 1
    countBrck = 0
    countLog = 0
    countComma = 0
    while ( posL >= 0 ):
        if mathList[posL] == ",":
            countComma += 1
        elif mathList[posL] == "(":
            countBrck += 1
        elif mathList[posL] == ")":
            countBrck -= 1
        elif mathList[posL] == "log":
            countLog += 1
        posL -= 1
    return countBrck - countLog < 1 and countLog - countComma > 0

def strToMathList(mathStr):
    mathList = []
    mathStr += "@"
    operations = "+-/*"
    brackets = "()"
    value = ""
    lastOpFlag = True
    floatFlag = False
    func = "log"
    posFunc = 0

    for symbol in mathStr:

        # print "check: " + symbol + " == " + func[posFunc] + ", posFunc: " + str(posFunc)

        if symbol.isdigit() or symbol == "-" and value == "" and lastOpFlag:
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
        elif symbol == "@":
            if value != "" and lastOpFlag:
                mathList.append(value)
            elif value == "":
                pass
            else:
                return Err["ErrOps"]
        elif symbol == func[posFunc]:
            posFunc += 1
            if posFunc == len(func):
                mathList.append("log")
                lastOpFlag = True
                posFunc = 0
        elif symbol == ",":
            logFlag = checkLogRight(mathList)
            if logFlag:
                if value != "" and lastOpFlag:
                    mathList.append(value)
                    value = ""
                lastOpFlag = True
                floatFlag = False
                mathList.append(symbol)
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
        lastElem = item
    if brackets != 0:
        return Err["ErrBracket"]

    return mathList

def mathListToPostfix(mathList):
    ExprData = []
    ExprOp = []
    prOp = {"+": 0, "-": 0, "*": 1, "/": 1, "(": 0, ")": 1, ",": 0, "log": 1}

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
                if item in ")":
                    popOp = ExprOp[::-1].index("(")
                    for pop in range(0, popOp):
                        ExprData.append(ExprOp.pop())
                    ExprOp.pop()
            elif item == ",":
                popOp = ExprOp[::-1].index("(")
                for pop in range(0, popOp):
                    ExprData.append(ExprOp.pop())
            elif len(ExprOp) > 0 and (
                        prOp[item] < prOp[ExprOp[-1]] or 
                        item in "-/" and prOp[item] == prOp[ExprOp[-1]]):
                try:
                    popOp = ExprOp[::-1].index("(")
                except ValueError:
                    popOp = len(ExprOp)
                for pop in range(0, popOp):
                    ExprData.append(ExprOp.pop())
            if item not in "),":
                ExprOp.append(item)
    return ExprData + ExprOp[::-1]

def opSum(a, b):
    return a + b

def opSub(a, b):
    return Decimal(a) - Decimal(b)

def opMult(a, b):
    return Decimal(a) * Decimal(b)

def opDiv(a, b):
    if b > 0 and b != 1 and a > 0:
        return Decimal(a) / Decimal(b)
    else:
        return Err["ErrZeroDiv"]

def opLog(a, b):
    if b != 1 and b > 0 and a > 0:
        return math.log( a, b)
    else:
        return Err["ErrLog"]

operations= {
    "+": opSum,
    "-": opSub,
    "*": opMult,
    "/": opDiv,
    "log": opLog
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
    elif step == "log":
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
