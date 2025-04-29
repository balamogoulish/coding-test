from sys import stdin
from collections import deque

n = int(stdin.readline())
m = int(stdin.readline())
tree = dict()

for i in range(1, n+1):
    tree[i]=[]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

# 1번 컴퓨터가 숙주임
visited = [False for _ in range(n+1)]
dq = deque([1])
visited[1] = True
answer = 0

while dq:
    curr = dq.popleft()
    answer += 1
    for nxt in tree[curr]:
        if not visited[nxt]:
            dq.append(nxt)
            visited[nxt] = True
print(answer-1)