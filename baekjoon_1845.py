import sys

# inputs = sys.stdin.read().splitlines()
# opNum = int(inputs[0])
# array = list(map(int, inputs[1]))

array = [1,3,2,4,5,6,8,7,9]
array = sorted(list(range(1, 251)), reverse=True)

def negative(v):
    return -v

def operate(arr, x, y):
    target = arr[x-1:y]
    target.reverse()
    arr[x-1:y] = map(negative, target)
    return

length = len(array)

exclusion = [-1, length]
# length = len(array)


for i in range(length):
    if array[i] == i+1:
        if i == exclusion[0]+1:
            exclusion[0] = i
    if array[-1-i] == length-i:
        if length-i-1 == exclusion[1]-1:
            exclusion[1] = length-i-1 

# print(exclusion)
# targetRange = exclusion[0] + 2, exclusion[1] + 1
# idxes = list(range(*targetRange))
# RangeCases = Pick(idxes)

def Pick(arr):
    ret = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            ret.append((arr[i], arr[j]))
    return ret

def GetRangeCases(arr):
    exclusion = [-1, length]
    for i in range(length):
        before = [exclusion[0], exclusion[1]]
        if array[i] == i+1:
            if i == exclusion[0]+1:
                exclusion[0] = i
                
        if array[-1-i] == length-i:
            if length-i-1 == exclusion[1]-1:
                exclusion[1] = length-i-1
        if before == exclusion:
            break
    targetRange = exclusion[0] + 2, exclusion[1] + 1
    idxes = list(range(*targetRange))
    RangeCases = Pick(idxes)
    return RangeCases

cases = GetRangeCases(range)
# print('cases ', cases, len(cases))
# cases = [(2,3), (4,5)]

from collections import deque

def GenerateProcess(cases, num):
    q = deque([(case, ) for case in cases])
    # print('initial q ',)
    while q:
        process = q.popleft()
        # print('process ', process)
        if len(process) == num:
            q.appendleft(process)
            break
        before = process[-1]
        # print('before', before)
        selection = tuple([sel for sel in cases if sel != before])
        # print('selection ', selection)
        
        for sel in selection:
            # print('to append ', (*process, sel ))
            q.append( (*process, sel ) )
    return q

# print(GenerateProcess(cases, 3))
# print(len(GenerateProcess(cases, 3)))

OperationPlan = GenerateProcess(cases, 3)
# print(OperationPlan)
NonInter = {}

def GetNonInter(cases):
    ret = {}
    for i in range(len(cases)-1):
        for j in range(i+1, len(cases)):
            if cases[i][1] < cases[j][0]:
                ret[cases[j], cases[i]] = cases[i], cases[j]
    return ret

NonInter = GetNonInter(cases)
print('NonInter', len(NonInter))

idx = 0
while idx < len(OperationPlan):
    r = 0
    while r < 3-1:
        # print(tuple(OperationPlan[idx][r:r+2]))
        if tuple(OperationPlan[idx][r:r+2]) in NonInter:
            # print('in')
            OperationPlan[idx] = (*OperationPlan[idx][:r], *NonInter[tuple(OperationPlan[idx][r:r+2])], *OperationPlan[idx][r+2:])
            if r > 0:
                if OperationPlan[idx][r] == OperationPlan[idx][r-1]:
                    OperationPlan.remove(OperationPlan[idx])
            elif r+2 <= len(OperationPlan[idx]):
                try:
                    if OperationPlan[idx][r+1] == OperationPlan[idx][r+2]:
                        OperationPlan.remove(OperationPlan[idx])
                except:
                    print(idx, r)
                    print(len(OperationPlan[idx]))
                    print(OperationPlan[idx])
                    raise IndexError   
            r = 0
        else:
            r += 1
    idx += 1

print(len(OperationPlan))
print(len(set(OperationPlan)))


    