from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
out_list = list(map(int, stdin.readline().split()))
q = deque([i for i in range(1, n+1)])

count = 0
i = 0
while i < m:
    if out_list[i] == q[0]: #찾는 요소가 가장 앞에 있는 경우
        q.popleft() #내보내고 cost는 들지 않음
        i += 1
    else: #찾는 요소가 가장 앞에 있지 않은 경우
        mid = int(len(q) / 2) 
        if q.index(out_list[i]) <= mid: #앞에서 찾는 게 빠른 경우
            q.append(q.popleft())
            count += 1
        else: #뒤에서 찾는 게 빠른 경우
            q.appendleft(q.pop())
            count += 1
print(count)