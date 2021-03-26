import sys

inputs = int(sys.stdin.read().splitlines()[0])
numList = [0, 1]
def Fibonacci(numList):
    while len(numList) < inputs + 1:
        numList.append(sum(numList[-2:]))
    return

if len(numList) > inputs:
    print(numList[inputs])
else:
    Fibonacci(numList)
    print(numList[-1])
