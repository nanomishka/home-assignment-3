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
            elif len(ExprOp) > 0 and prOp[item] < prOp[ExprOp[-1]]:
                popOp = ExprOp[::-1].index("(")
                for pop in range(0, popOp):
                    ExprData.append(ExprOp.pop())
            if item != ")":
                ExprOp.append(item)

    mathList = StrToMathList(mathData)
    return ExprData + ExprOp[::-1]

mathData = "((1+2)*(3+4)*5+6)/7*(6+7)"
mathList = StrToMathList(mathData)
postfix = MathListToPostfix(mathList)

print postfix
        



















