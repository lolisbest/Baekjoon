import sys

inputs = sys.stdin.read().splitlines()

n = int(inputs[0])
nums = list(inputs[1].split())
m = int(inputs[2])
targets = list(inputs[3].split())

print(inputs)

A = {}

for idx in nums:
    A[idx] = True

for target in targets:
    try:
        if A[target]:
            print(1)
    except:
        print(0)
        

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
# 
# 1
# 1
# 0
# 0
# 1
