from sys import stdin

#[숫자: [빈도 수, 처음 등장한 인덱스]]

n, c = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
answer = {}

for i in range(n):
    if arr[i] not in answer:
        answer[arr[i]] = [0, i]
    answer[arr[i]][0]+=1

answer = sorted(answer.items(), key=lambda x: (-x[1][0], x[1][1]))
for a in answer:
    for _ in range(a[1][0]):
        print(a[0], end=' ')