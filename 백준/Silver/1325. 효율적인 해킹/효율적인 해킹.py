from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
tree = {}
answer = []
max_cnt = 0

for _ in range(m):
    child, parent = map(int, stdin.readline().split())
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)

for i in range(1, n+1):
    cnt = 0
    visited = [False for _ in range(n+1)]
    visited[i] = True
    dq = deque([i])
    
    while dq:
        parent = dq.popleft()
        cnt+=1
        # print('child', parent)
        if parent not in tree:
            continue
        for child in tree[parent]:
            if not visited[child]:
                dq.append(child)
                visited[child] = True
    
    if max_cnt<cnt:
        max_cnt = cnt
        answer = [i]
    elif max_cnt==cnt:
        answer.append(i)
        
        
answer.sort()
for a in answer:
    print(a, end=' ')
        