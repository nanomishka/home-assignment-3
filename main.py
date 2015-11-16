from calc import *

if __name__ == '__main__':
    while True:
        mathData = raw_input()
        if mathData != "":
            print calculate(mathData)
        else:
            break
