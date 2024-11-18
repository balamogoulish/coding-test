# 시리얼 정렬
#1. X와 Y의 길이가 다르면, 짧은 것이 먼저 옴
#2. 숫자인 것만 더해서 작은 순으로 옴
#3. 사전순으로 정렬 (숫자가 알파벳보다 우선됨)


from sys import stdin

n = int(stdin.readline())
arr = []

for _ in range(n):
    k = stdin.readline().split('\n')[0]
    sum_s = 0
    for s in k:
        if s.isdigit():
            sum_s+=int(s)
    arr.append([k, sum_s])

arr.sort(key=lambda x: (len(x[0]), x[1], x[0]))

for a in arr:
    print(a[0])