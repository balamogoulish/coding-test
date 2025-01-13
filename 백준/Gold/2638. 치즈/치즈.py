'''
1. 두 변 이상이 외부와 닿아있다면 한 시간 후 사라짐
    그러나 치즈로 닫혀 있는 공간은 내부로 처리함
    => 어떻게 치즈로 닫혀 있는 공간을 처리할 것인가?
    a. 0인 구역을 구함
    b. 가장 자리인 경우 외부로 처리되므로 불가 -> ny, nx가 좌표를 벗어나면 가장자리임
    c. 치즈로 닫혀있는 공간은 2로 처리함
    d. 치즈는 0과 맞닿은 면의 수만 계산해서 2개 이상 닿아있는 경우, 0으로 바꿈꿈
'''

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
cheese = [list(map(int, stdin.readline().split())) for _ in range(n)]
tmp = []
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def checkInside(x, y):
    zero = [[x, y]]
    q = deque([[x, y]])
    isOutside = False
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if cheese[ny][nx]==0 and not visited[ny][nx]:
                    q.append([nx, ny])
                    visited[ny][nx] = True
                    zero.append([nx, ny])
            else:
                isOutside = True
    if not isOutside:
        for z in zero:
            tmp[z[1]][z[0]] = 2

        
def isCheese():
    for c in cheese:
        if 1 in c:
            return True
answer = 0
while isCheese():
    visited = [[False for _ in range(m)] for _ in range(n)]
    tmp = [[a for a in c] for c in cheese]
    # tmp 배열에 내외부를 판별하여 넣는다. 0은 외부, 2는 내부 1은 치즈
    for y in range(n):
        for x in range(m):
            if not visited[y][x] and cheese[y][x]==0:
                visited[y][x]=True
                checkInside(x, y)
    
    # cheese와 tmp를 확인하면서 외부 두 면과 닿아있는 치즈를 0으로 바꾼다.
    for y in range(n):
        for x in range(m):
            if cheese[y][x]==1:
                cnt = 0
                for i in range(4):
                    ny, nx = y+dy[i], x+dx[i]
                    if 0<=ny<n and 0<=nx<m:
                        if tmp[ny][nx]==0:
                            cnt+=1
                    else:
                        cnt+=1
                if cnt>=2:
                    cheese[y][x] = 0
    answer+=1
print(answer)