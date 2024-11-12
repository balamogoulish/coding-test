from sys import stdin

n = int(stdin.readline())
arr = []

for _ in range(n):
    arr.append(float(stdin.readline()))

for i in range(1, n):
    arr[i] = max(arr[i-1]*arr[i], arr[i])

print('%.3f'%(max(arr)))