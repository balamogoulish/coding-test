from sys import stdin

n, m = map(int, stdin.readline().split())

h = set([])
cnt =0
hs=set([])
for _ in range(n):
    x = stdin.readline().split('\n')
    h.add(x[0])
for _ in range(m):
    a = stdin.readline().split('\n')[0]
    if a in h:
      cnt+=1
      hs.add(a)
print(cnt)
hs = sorted(hs)
for i in hs:
    print(i)