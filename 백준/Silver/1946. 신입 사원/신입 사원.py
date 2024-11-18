from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    arr = []
    m = int(stdin.readline())
    answer = m
    for _ in range(m):
        arr.append(list(map(int, stdin.readline().split())))
    arr=sorted(arr)
    k = arr[0][1]
    for a in arr:
        if k<a[1]:
            answer-=1
        k = min(k, a[1])
    print(answer)