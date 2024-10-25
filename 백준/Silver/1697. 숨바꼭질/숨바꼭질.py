from collections import deque

N, K = input().split()
n, k = int(N), int(K)
max_num = 100000
visited = [0]*(max_num+1)

def bfs(): #현재 위치와 이동 횟수
    q = deque()
    q.append(n)
    while q:
        x=q.popleft()
        if x==k:
            print(visited[x])
            break
        else:
            for j in (x-1, x+1, x*2):
                if 0<=j<=max_num and not visited[j]:
                    visited[j] = visited[x]+1
                    q.append(j)
 
bfs()