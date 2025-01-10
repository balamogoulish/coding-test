from sys import stdin
from collections import deque

n = int(stdin.readline())
non_root_tree = [[] for _ in range(n+1)]
tree = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    non_root_tree[a].append(b)
    non_root_tree[b].append(a)


parent_q = deque([1])
while parent_q:
    parent = parent_q.popleft()
    visited[parent] = True
    children = non_root_tree[parent]
    # print('p',parent, children)
    for c in children:
        if not visited[c]:
            parent_q.append(c)
            tree[c]=parent

for i in range(2, n+1):
    print(tree[i])