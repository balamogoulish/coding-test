from sys import stdin

n, m = map(int, stdin.readline().split())
S = [stdin.readline().strip() for _ in range(n)]
test = [stdin.readline().strip() for _ in range(m)]

answer = 0

for t in test:
    if t in S:
        answer +=1
print(answer)