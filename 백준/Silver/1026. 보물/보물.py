from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
a = sorted(a)
b = sorted(b, reverse=True)

ans = 0
for i in range(n):
    ans+= a[i]*b[i]
print(ans)