import sys

inputs = sys.stdin.read().splitlines()

def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n-1)

# print(inputs)
print(Factorial(int(inputs[0])))

