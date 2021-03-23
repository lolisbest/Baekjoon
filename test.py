# n = 10

# ret = [['JJB']*n]*n

# for line in ret:
#     for e in line:
#         print(id(e)) 




import sys

inputs = sys.stdin.read().splitlines()
N, M = map(int, inputs[0].split())

matrix = [list(map(int, nums.split())) for nums in inputs[1:1+N]]
commands = inputs[1+N:1+N+M]

def MakeTable(mat):
    n = len(mat)
    
    print(mat)
    print(matrix)

    # ret = [[None]*n]*n
    ret0 = [[None for _ in range(n)]]*2
    ret1 = [[1,2,3]]*2


    for line0 in ret0:
        print(id(line0))
        
    for line1 in ret1:
        print(id(line1))
    
    return 0

    numSum = 0
    for row in range(n):
        # print('mat ', mat[row][0])
        # print()
        numSum += mat[row][0]

        ret[row][0] = numSum
        for line in ret:
            print(id(line))
            print()
        print(row, numSum)

    for line in ret:
        print(line)

    # numSum = 0
    # for column in range(n):
    #     numSum += matrix[0][column]
    #     ret[0][column] = numSum

    # for line in ret:
    #     print(line)

    # for row in range(1, n):
    #     for column in range(1, n):
    #         print(row, column)
    #         ret[row][column] = ret[row][column-1] + ret[row-1][column] - ret[row-1][column-1] + mat[row][column]
    
    # return ret
print(MakeTable(matrix))