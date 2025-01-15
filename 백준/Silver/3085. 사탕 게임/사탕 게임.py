from sys import stdin

n = int(stdin.readline())
candies = [[c for c in stdin.readline().strip()] for _ in range(n)]

#연속된 부분 계산 함수
def checkCandy(x, y): 
    ans = 0
    cnt_x = 1
    for dx in range(1, n):
        if candies[y][dx-1]!=candies[y][dx]:
            ans = max(ans, cnt_x)
            cnt_x=1
        else:
            cnt_x+=1
    ans = max(ans, cnt_x)
    cnt_y = 1
    for dy in range(1, n):
        if candies[dy-1][x]!=candies[dy][x]:
            ans = max(ans, cnt_y)
            cnt_y=1
        else:
            cnt_y+=1
    ans = max(ans, cnt_y)
    return ans

def exchangeCandy(x, y, nx, ny):
    tmp = candies[y][x]
    candies[y][x] = candies[ny][nx]
    candies[ny][nx] = tmp
    
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

answer = 0
for y in range(n):
    for x in range(n):
        answer = max(answer, checkCandy(x, y))
        curr = candies[y][x]
        for i in range(2):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and curr!=candies[ny][nx]:
                exchangeCandy(x, y, nx, ny)
                answer = max(answer, checkCandy(x, y))
                answer = max(answer, checkCandy(nx, ny))

                exchangeCandy(x, y, nx, ny)
                if answer == n:
                    print(answer)
                    exit()
print(answer)
