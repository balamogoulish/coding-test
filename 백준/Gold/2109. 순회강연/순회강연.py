from sys import stdin

n = int(stdin.readline())
answer = [0 for _ in range(10001)]

# 기한이 빠른 순대로, 가격이 높은 순대로 정렬
PDs = sorted([list(map(int, stdin.readline().split())) for _ in range(n)], key=lambda x: (-x[0],x[1]))

for pd in PDs:
    p, d = pd[0], pd[1]
    for i in range(d):
        if answer[d-i]==0:
            answer[d-i]=p
            break

print(sum(answer))