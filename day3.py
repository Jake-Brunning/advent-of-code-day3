import re

def readFile(filepath: str) -> str:
    file = open(filepath, 'r')
    return file.read()

def performAMul(input: str) ->int:
    input = input.removeprefix('mul(')
    input = input.removesuffix(')')
    input = input.split(',')
    num1 = int(input[0])
    num2 = int(input[1])
    return num1 * num2

def sumMults(input: str) -> int:
    input = extractInfo(input)
    total = 0

    for x in input:
        total += performAMul(x)
    
    return total

def extractInfo(input: str) -> str:
    #usse relular expression to make my life easier
    return re.findall("mul\([0-9]*,[0-9]*\)|do\(\)|don't\(\)", input) 

def evaluateExpression(input: str) -> str:
    return input[0:3]

def performExpressions(input: str):
    input = extractInfo(input)
    total = 0
    performMult = True

    for x in input:
        expr = evaluateExpression(x)
        if expr == "mul" and performMult:
            total += performAMul(x)
        elif expr == "do(":
            performMult = True
        elif expr == "don":
            performMult = False
    
    return total

if __name__ == '__main__':
    print(performExpressions(readFile("input.txt")))