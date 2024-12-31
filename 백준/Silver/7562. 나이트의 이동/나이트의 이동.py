from sys import stdin
from collections import deque

T = int(stdin.readline())
dx = [2, 2, 1 ,1, -2, -2, -1, -1]
dy = [1, -1, 2, -2, 1, -1, 2, -2]

for _ in range(T):
    I = int(stdin.readline()) #체스판의 한 변의 길이 
    start_x, start_y = map(int, stdin.readline().split()) #나이트가 현재 있는 칸
    end_x, end_y = map(int, stdin.readline().split()) #나이트가 이동하려는 칸 
    visited = [[-1 for _ in range(I)] for _ in range(I)]
    
    q = deque([[start_x, start_y, 0]])
    
    while q:
        curr_x, curr_y, curr_cnt = q.popleft()
        if curr_x==end_x and curr_y==end_y:
            print(curr_cnt)
            break
        elif visited[curr_y][curr_x]!=-1:
            continue
        visited[curr_y][curr_x] = curr_cnt
        for i in range(8):
            nx, ny = curr_x+dx[i], curr_y+dy[i]
            if 0<=nx<I and 0<=ny<I :
                if visited[ny][nx]==-1:
                    q.append([nx, ny, curr_cnt+1])
