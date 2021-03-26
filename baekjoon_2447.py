import sys


N = int(sys.stdin.read().splitlines()[0])
starPic = [['*']*N for _ in range(N)]

def Star(rowList, columnList):
    if len(rowList) == 1 and len(columnList) == 1:
        return
    else: 
        currentN = len(rowList)
        unitN = currentN//3
        rowList = [[rowList[j] for j in range(i*unitN, (i+1)*unitN)] for i in range(3)]
        columnList = [[columnList[j] for j in range(i*unitN, (i+1)*unitN)] for i in range(3)]
        pair = [[rowList[i], columnList[j]] for j in range(len(columnList)) for i in range(len(rowList))]
        blankSection = pair.pop(4)
        for row in blankSection[0]:
            for colomn in blankSection[1]:
                starPic[row][colomn] = ' '
        for rl, cl in pair: 
            Star(rl, cl)
    return

Rows = list(range(N))
Cols = list(range(N))

Star(Rows, Cols)

# for line in starPic: 
#     for pic in line:
#         print(pic, end='')
#     print(end='\n')

for line in starPic:
    print(''.join(line))
