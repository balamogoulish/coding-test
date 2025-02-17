from sys import stdin
from collections import deque

n, l, r = map(int, stdin.readline().split())
countries = [list(map(int, stdin.readline().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0

# BFS를 활용하여 연합을 찾는 함수
def get_allies_bfs(sx, sy, visited):
    queue = deque([(sx, sy)])
    ally = [(sx, sy)]
    visited.add((sx, sy))
    population_sum = countries[sy][sx]
    
    while queue:
        cx, cy = queue.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                diff = abs(countries[cy][cx] - countries[ny][nx])
                if l <= diff <= r:
                    queue.append((nx, ny))
                    ally.append((nx, ny))
                    visited.add((nx, ny))
                    population_sum += countries[ny][nx]

    return ally, population_sum

while True:
    ally_cnt = 0
    visited = set()
    move_happened = False
    
    # 연합 찾기
    for y in range(n):
        for x in range(n):
            if (x, y) not in visited:
                ally, population_sum = get_allies_bfs(x, y, visited)
                if len(ally) > 1:
                    ally_cnt += 1
                    move_happened = True
                    new_population = population_sum // len(ally)
                    for ax, ay in ally:
                        countries[ay][ax] = new_population

    if not move_happened:
        break
    
    answer += 1

print(answer)
