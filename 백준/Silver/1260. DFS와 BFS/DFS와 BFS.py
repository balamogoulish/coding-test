# DFS 경로, BFS 경로 출력
# curr와 연결된 곳이 여러 개인 경우, 작은 순부터 => 처음 넣을 때 정렬 후 넣기
from sys import stdin
from collections import deque

n, m, v = map(int, stdin.readline().split())
tree = dict()

for i in range(1, n+1):
    tree[i] = []
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
for i in range(1,n+1):
    tree[i] = sorted(tree[i])


def dfs_root(start):
    visited = [False for _ in range(n+1)]
    root = []
    
    def dfs(curr):
        visited[curr] = True
        root.append(curr)
        for nxt in tree[curr]:
            if not visited[nxt]:
                dfs(nxt)
    dfs(start)
    return root

def bfs_root(start):
    visited = [False for _ in range(n+1)]
    dq = deque([start])
    root = []
    visited[start] = True
    
    while dq:
        curr = dq.popleft()
        root.append(curr)
        for nxt in tree[curr]:
            if not visited[nxt]:
                dq.append(nxt)
                visited[nxt] = True
    return root
    
dfs_list = dfs_root(v)
bfs_list = bfs_root(v)

for d in dfs_list:
    print(d, end=" ")
print()
for d in bfs_list:
    print(d, end=" ")
    