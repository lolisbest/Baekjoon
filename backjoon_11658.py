import sys

m_input = '''4 5
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
1 2 2 3 4
0 2 3 7
1 2 2 3 4
0 3 4 5
1 3 4 3 4'''

m_input = '''1 2
1
1 1 1 1 1
0 1 1 7'''

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

input_list = sys.stdin.read().splitlines()

n = int(input_list[0].split(' ')[0])
m = int(input_list[0].split(' ')[1])

mat = []
for row in input_list[1:1+n]:
    mat.extend(map(int, row.split(' ')))

commands = []
for row in input_list[1+n:]:
    command = list(map(int, row.split(' ')))
    commands.extend([[command[0], command[1:]]])
ret = ""
# tmp = 0

for command in commands:
    if command[0] == 1:
        tmp = 0
        s_i = command[1][0]
        s_j = command[1][1]
        e_i = command[1][2]
        e_j = command[1][3]
        for offset in range(e_i-s_i+1):
            base_i = s_i-1
            tmp += sum(mat[(base_i+offset)*n+(s_j-1):(base_i+offset)*n+(e_j)])
        ret += str(tmp) + "\n"
    elif command[0] == 0:
        t_i = command[1][0]
        t_j = command[1][1]
        t_n = command[1][2]
        mat[(t_i-1)*n + (t_j-1)] = t_n
    else:
        pass

output = ret[:-1].split('\n')
for w in output:
    print(w)


