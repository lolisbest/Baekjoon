import sys

N = int(sys.stdin.read().splitlines()[0])

def Hanoi(floor, src, dst, plan):
    
    # print('{} : {} -> {}'.format(floor, src, dst))
    
    if floor != 1:
        location = [i for i in [1,2,3] if i not in [src, dst]]
        Hanoi(floor-1, src, location[0], plan)
        plan.append((src, dst))
        Hanoi(floor-1, location[0], dst, plan)
    else:
        plan.append((src, dst))
    return
answer = []
Hanoi(N, 1, 3, answer)

print(len(answer))
for pair in answer:
    print(*pair)
