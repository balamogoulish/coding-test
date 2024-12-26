from sys import stdin

n = int(stdin.readline())
apt = []
visited = [[False for _ in range(n)] for _ in range(n)]
answer = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = []

# 입력을 정수형 이차원 배열로 저장 
for _ in range(n):
    st_apt = stdin.readline().strip()
    li_apt = []
    for t in st_apt:
        li_apt.append(int(t))
    apt.append(li_apt)
    
def bfs(x, y, k):
    visited[y][x]=True
    cnt[k]+=1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and apt[ny][nx]==1:
            if not visited[ny][nx]:
                bfs(nx, ny, k)
                
    
for y in range(n):
    for x in range(n):
        if not visited[y][x] and apt[y][x]==1:
            answer+=1
            cnt.append(0)
            bfs(x, y, len(cnt)-1)
print(answer)
cnt = sorted(cnt)
for c in cnt:
    print(c)
