from sys import stdin

n = 1000-int(stdin.readline())
coins = [500, 100, 50, 10, 5, 1]

ans = 0
for c in coins:
    ans+=n//c
    n = n%c
print(ans)
