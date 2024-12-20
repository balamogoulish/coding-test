from sys import stdin

n, m =map(int, stdin.readline().split())
p = [stdin.readline().strip() for _ in range(n)]

for _ in range(m):
    q = stdin.readline().strip()
    if q.isdigit():
        print(p[int(q)-1])
    else:
        print(p.index(q)+1)