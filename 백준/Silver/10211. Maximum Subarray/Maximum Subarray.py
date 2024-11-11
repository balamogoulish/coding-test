from sys import stdin

n = int(stdin.readline())
for _ in range(n):
    T = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    for i in range(1, T):
        arr[i]=max(arr[i-1]+arr[i], arr[i])
    print(max(arr))