from sys import stdin

n, k = map(int, stdin.readline().split())
coins = []
ans=0

for _ in range(n):
    coins.append(int(stdin.readline()))
coins = sorted(coins, reverse=True)
for c in coins:
    ans += k//c
    k = k%c
    if k==0:
        print(ans)
        break
    