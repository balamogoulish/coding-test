from sys import stdin
from collections import deque

n = int(stdin.readline())
cycles = deque([(stdin.readline().strip()) for _ in range(n)])
answer = [cycles.popleft()]

while cycles:
    curr = deque(cycles.popleft())
    isAlready = False
    tmp = ''
    for _ in range(len(curr)):
        curr.append(curr.popleft())
        tmp = ''
        for c in curr:
            tmp+=c
        if tmp in answer:
            isAlready = True
            break
    if not isAlready:
        answer.append(tmp)
print(len(answer))
