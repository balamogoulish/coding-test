from sys import stdin

n = int(stdin.readline())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]

def dfs(curr):
    v=[curr]
    visited = [False for _ in range(n)]
    while v:
        i = v.pop()
        for j in range(n):
            if graph[i][j]==1 and visited[j]==False:
                v.append(j)
                graph[curr][j]=1
                visited[j]=True

for i in range(n):
    dfs(i)
    for g in graph[i]:
        print(g, end=' ')
    print()
    