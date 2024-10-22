#https://www.acmicpc.net/problem/2798

from itertools import combinations

n, m = map(int, input().split())

cards = list(map(int, input().split()))
comb = list(combinations(cards, 3))
ans = 0

for c in comb:
    temp = sum(c)
    if ans < temp <= m:
        ans = temp
print(ans)
