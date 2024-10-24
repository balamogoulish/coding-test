# https://www.acmicpc.net/problem/11399
from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr = sorted(arr)

ans = 0
for i in range(len(arr)):
    ans+=sum(arr[:+1+i])
print(ans)