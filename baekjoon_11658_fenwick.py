import sys

inputs = sys.stdin.read().splitlines()
N, M = map(int, inputs[0].split())

matrix = [list(map(int, nums.split())) for nums in inputs[1:1+N]]
commands = inputs[1+N:1+N+M]

TwoDimFenWickTree = [[0 for _ in range(N)] for _ in range(N)]

def UpdateFenWickTree(x, y, v): #  0 < x < N
    row = x
    
    if v == 0:
        return 

    while row <= N:
        column = y
        while column <= N:
            TwoDimFenWickTree[row-1][column-1] += v
            column += (column & -column)
        row += (row & -row)
    return


def GetAreaSum(x, y): #  0 < x < N
    row = x
    retSum = 0
    while row > 0:
        column = y
        while column > 0:
            retSum += TwoDimFenWickTree[row-1][column-1] 
            column -= (column & -column)
        row -= (row & -row)
    return retSum


def printTree():
    for line in TwoDimFenWickTree:
        for e in line:
            print(e, end='\t')
        print(end='\n')
    return 

for row in range(N):
    for column in range(N):
        UpdateFenWickTree(row+1, column+1, matrix[row][column])

for command in commands:

    if command[0] == '0':
        _, x, y, v = map(int, command.split())
        UpdateFenWickTree(x, y, v - matrix[x-1][y-1])
        matrix[x-1][y-1] = v

    elif command[0] == '1':
        _, sx, sy, dx, dy = map(int, command.split())
        areaSum = GetAreaSum(dx, dy) - GetAreaSum(dx, sy-1) - GetAreaSum(sx-1, dy) + GetAreaSum(sx-1, sy-1)
        print(areaSum)
    else:
        pass 



