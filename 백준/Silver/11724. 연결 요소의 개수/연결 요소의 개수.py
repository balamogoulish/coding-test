from sys import stdin
import sys
sys.setrecursionlimit(10 ** 5)

n, m = map(int, stdin.readline().split())
graph = {}
visited = [0 for _ in range(n+1)]
answer = [0]

for i in range(1, n+1):
    graph[i] = []
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(curr):
    if visited[curr]==0:
        answer[0] += 1
        visited[curr]=1

    for nxt in graph[curr]:
        if visited[nxt]==1: #다음 노드를 가봤다면 다시 갈 필요 없음
            continue
        else: #다음 노드를 안 가봤다면 연결되었으니 가봤다고 하고 dfs 실행
            visited[nxt]=1
            dfs(nxt)

for g in graph:
    if visited[g]==0:
        dfs(g)
print(answer[0])
    