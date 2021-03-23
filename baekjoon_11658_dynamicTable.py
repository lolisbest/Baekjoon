
m_input = '''
4 5
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
1 2 2 3 4
0 2 3 7
1 2 2 3 4
0 3 4 5
1 3 4 3 4
'''

m_input = '''
1 2
1
1 1 1 1 1
0 1 1 7
'''

m_input = '''
5 6
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9
1 4 4 4 4
0 1 1 9
0 5 5 1
1 1 1 1 4
0 4 4 2
1 1 1 4 1
1 1 1 4 4
'''


import sys

inputs = sys.stdin.read().splitlines()
N, M = map(int, inputs[0].split())

matrix = [list(map(int, nums.split())) for nums in inputs[1:1+N]]
commands = inputs[1+N:1+N+M]

def MakeTable(mat):
    n = len(mat)

    ret = [[None for _ in range(n)] for _ in range(n)]

    numSum = 0
    for row in range(n):
        numSum += mat[row][0]
        ret[row][0] = numSum

    numSum = 0
    for column in range(n):
        numSum += mat[0][column]
        ret[0][column] = numSum

    for row in range(1, n):
        for column in range(1, n):
            ret[row][column] = ret[row][column-1] + ret[row-1][column] - ret[row-1][column-1] + mat[row][column]
        
    return ret


def UpdateTable(inputMatrix, dynamicTable, x, y, newValue):
    n = len(dynamicTable)

    diff = newValue - inputMatrix[x][y]
    
    if diff == 0:
        return 

    inputMatrix[x][y] = newValue

    for row in range(x, n):
        for column in range(y, n):
            dynamicTable[row][column] += diff

    return    

dynamicSumTable = MakeTable(matrix)

for command in commands:

    if command[0] == '0':
        _, x, y, v = map(int, command.split())
        UpdateTable(matrix, dynamicSumTable, x-1, y-1, v)
    elif command[0] == '1':
        _, sx, sy, dx, dy = map(int, command.split())
        if sx == 1 and sy == 1:
            areaSum = dynamicSumTable[dx-1][dy-1]
        elif sx == 1 and sy != 1:
            areaSum = dynamicSumTable[dx-1][dy-1] - dynamicSumTable[dx-1][sy-2]
        elif sx != 1 and sy == 1:
            areaSum = dynamicSumTable[dx-1][dy-1] - dynamicSumTable[sx-2][dy-1]
        else:
            areaSum = dynamicSumTable[dx-1][dy-1] - dynamicSumTable[sx-2][dy-1] - dynamicSumTable[dx-1][sy-2] + dynamicSumTable[sx-2][sy-2]
        print(areaSum)

    else:
        pass       




