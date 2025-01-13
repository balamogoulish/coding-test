from sys import stdin
from itertools import combinations

n = int(stdin.readline())
garden = [list(map(int, stdin.readline().split())) for _ in range(n)]
comb = []

answer = 3001 #최대 비용+1

dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]

def check(flower):
    tmp = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for f in flower:
        cx, cy = f
        for i in range(5):
            nx, ny = cx+dx[i], cy+dy[i]
            if not visited[ny][nx]:
                tmp+=garden[ny][nx]
                visited[ny][nx] = True

            else:
                return 3001
    return tmp

#가장 자리를 제외한 좌표를 comb에 넣음
for y in range(1, n-1):
    for x in range(1, n-1):
        comb.append([x, y])
#조합을 통해 comb에서 3개의 좌표를 뽑음
for c in combinations(comb, 3):
    answer = min(answer, check(c))

print(answer)