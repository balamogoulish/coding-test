from sys import stdin
from itertools import permutations

n = int(stdin.readline()) #수의 개수
A = list(map(int, stdin.readline().split())) #수
OP_cnt = list(map(int, stdin.readline().split())) #+, -, *, / 의 수
OP = []

for _ in range(OP_cnt[0]):
    OP.append('+')
for _ in range(OP_cnt[1]):
    OP.append('-')
for _ in range(OP_cnt[2]):
    OP.append('*')
for _ in range(OP_cnt[3]):
    OP.append('/')

OP = set(list(permutations(OP, len(OP))))

min_answer = 1000000001
max_answer = -1000000001

for op in OP:
    tmp_answer = A[0]
    for i in range(n-1):
        if op[i]=='+':
            tmp_answer+=A[i+1]
        elif op[i]=='-':
            tmp_answer-=A[i+1]
        elif op[i]=='*':
            tmp_answer*=A[i+1]
        elif op[i]=='/':
            if tmp_answer<0:
                x = -tmp_answer
                tmp_answer= (x//A[i+1])*(-1)
            else:
                tmp_answer//=A[i+1]
    min_answer = min(min_answer, tmp_answer)
    max_answer = max(max_answer, tmp_answer)

print(max_answer)
print(min_answer)