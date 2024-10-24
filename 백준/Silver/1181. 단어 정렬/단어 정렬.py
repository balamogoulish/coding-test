#https://www.acmicpc.net/problem/1181

n = int(input())
arr = set([])

for _ in range(n):
    arr.add(input())
arr = sorted(arr, key=lambda x: (len(x),x))
for a in arr:
    print(a)