from sys import stdin

n, m, k = map(int, stdin.readline().split())
ground = [[5] * n for _ in range(n)]  # 각 칸의 초기 양분
A = [list(map(int, stdin.readline().split())) for _ in range(n)]  # 겨울에 추가되는 양분
trees = [[[] for _ in range(n)] for _ in range(n)]  # 나무의 나이 저장

# 초기 나무 정보 입력
for _ in range(m):
    x, y, age = map(int, stdin.readline().split())
    trees[x-1][y-1].append(age)

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, -1, 0, 1, -1, 1, -1, 0]

for _ in range(k):
    # 봄 & 여름
    for y in range(n):
        for x in range(n):
            if not trees[y][x]:  # 나무가 없으면 넘어감
                continue
            trees[y][x].sort()  # 나이가 어린 나무부터 정렬
            alive, dead_food = [], 0
            for age in trees[y][x]:
                if ground[y][x] >= age:  # 양분이 충분한 경우
                    ground[y][x] -= age
                    alive.append(age + 1)  # 나이 증가
                else:  # 양분 부족으로 죽음
                    dead_food += age // 2
            trees[y][x] = alive
            ground[y][x] += dead_food  # 죽은 나무의 나이를 양분으로 추가

    # 가을
    for y in range(n):
        for x in range(n):
            for age in trees[y][x]:
                if age % 5 == 0:  # 5의 배수인 경우 번식
                    for i in range(8):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < n and 0 <= ny < n:
                            trees[ny][nx].append(1)  # 새로 심어진 나무

    # 겨울
    for y in range(n):
        for x in range(n):
            ground[y][x] += A[y][x]  # 양분 추가

# 최종 나무 개수 계산
answer = sum(len(t) for row in trees for t in row)
print(answer)
