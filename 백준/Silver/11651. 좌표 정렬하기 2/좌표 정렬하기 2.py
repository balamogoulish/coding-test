from sys import stdin

n = int(stdin.readline())
arr = []
for _ in range(n):
    x, y = (map(int, stdin.readline().split()))
    arr.append([y, x])
arr= sorted(arr)

for a in arr:
    print(a[1], a[0])