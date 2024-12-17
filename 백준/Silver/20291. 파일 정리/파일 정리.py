from sys import stdin
from collections import Counter

#1. 확장자 별 파일 수
#2. 확장자를 사전 순 정렬

n = int(stdin.readline())
exs = []

for _ in range(n):
    ex = stdin.readline().split('.')[1]
    ex = ex.split('\n')[0]
    exs.append(ex)
exs = Counter(exs)
exs = sorted(exs.items(), key=lambda x: x[0])

for e in exs:
    print(e[0], e[1])