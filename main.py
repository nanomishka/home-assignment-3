from calc import *

if __name__ == '__main__':
    while True:
        # try:
        mathData = raw_input()
        if mathData != "":
            mathList = StrToMathList(mathData)
            postfix = MathListToPostfix(mathList)
            print postfix
            print "Result: " + str(evalute(postfix))
        else:
            break