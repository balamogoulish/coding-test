from sys import stdin
from collections import deque

n = int(stdin.readline())
parents = list(map(int, stdin.readline().split()))
tree = {}
remove_node = int(stdin.readline())
root_node = -1

answer = 0

for child in range(n):
    if parents[child] == -1:
        root_node = child
        continue
    if parents[child] not in tree:
        tree[parents[child]] = []
    tree[parents[child]].append(child)

dq = deque([root_node])

while dq:
    parent = dq.popleft()
    if parent == remove_node:
        break
    if parent not in tree: #parent가 자식이 없는 경우 leaf_node
        answer+=1
        continue
    
    for child in tree[parent]:
        if child == remove_node: #자식 노드가 제거된 노드인 경우 큐에 추가하지 않음  
            if len(tree[parent])==1: #제거된 노드가 유일한 자식인 경우 parent는 leaf_node
                answer+=1
        else:
            dq.append(child)

print(answer)
            