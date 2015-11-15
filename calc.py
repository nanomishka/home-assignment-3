def StrToMathList(str):
    mathList = []
    str += "@"
    operations = "+-/*"
    value = ""

    for symbol in str:
        if symbol.isdigit():
            value += symbol
        elif symbol in operations:
            mathList.append(int(value))
            mathList.append(symbol)
            value = ""
        elif symbol == "@":
            mathList.append(int(value))

    return mathList

def MathListToPostfix(mathList):
    ExprData = []
    ExprOp = []

    for item in mathList:
        if isinstance(item, int):
            ExprData.append(item)
        else:
            ExprOp.append(item)

    mathList = StrToMathList(mathData)
    return ExprData + ExprOp[::-1]

mathData = "1 + 2 - 3 * 4"
mathList = StrToMathList(mathData)
postfix = MathListToPostfix(mathList)

print postfix
        



















