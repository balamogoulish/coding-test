from sys import stdin
from collections import deque

n = int(stdin.readline())
meets = deque(sorted([list(map(int, stdin.readline().split())) for _ in range(n)], key=lambda x: (x[1], x[0])))
prev_end = -1
answer = 0

# 이전 미팅이 끝난 시간보다는 느리고 끝나는 시간이 빠른 순대로 확인함
while meets:
    start, end = meets.popleft()
    if start >= prev_end:
        prev_end = end
        answer+=1
print(answer)