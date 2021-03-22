# EOFError
import sys

inputs = sys.stdin.read().splitlines()

print('inputs:', inputs)

N = int(inputs[0])

B = list(map(int, inputs[1].split()))

check = [False] * N
sortedB = sorted(B)

P = []
# print(check)
# print(sortedB)
# print(B)

for element_B in B:
    
    order = sortedB.index(element_B)
    
    while check[order]:
        order += 1
    
    P.append(str(order))
    check[order] = True

print(' '.join(P))




# 3
# 2 3 1



# 1 2 0

