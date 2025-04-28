
from sys import stdin
from collections import deque

n, m, k, x = map(int, stdin.readline().split()) #도시수, 도로수, 거리 정보, 출발 도시
cities = dict()
for i in range(1, n+1):
    cities[i]=[]

for _ in range(m):
    start, end = map(int, stdin.readline().split())
    cities[start].append(end)

visited = [300001 for _ in range(n+1)]
dq = deque([[x, 0]])
visited[x] = 0

answer = []

while dq:
    curr_node, curr_dist = dq.popleft()
    for nxt_node in cities[curr_node]:
        if visited[nxt_node] > curr_dist+1:
            visited[nxt_node] = curr_dist+1
            dq.append([nxt_node, curr_dist+1])
            if k==curr_dist+1:
                answer.append(nxt_node)
if len(answer)==0:
    print(-1)
else:
    for s in sorted(answer):
        print(s)