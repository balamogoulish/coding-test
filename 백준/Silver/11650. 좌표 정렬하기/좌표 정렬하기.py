#https://www.acmicpc.net/problem/1181

n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
arr = sorted(arr, key=lambda a: (a[0], a[1]))

for a in arr:
    print(a[0], a[1])