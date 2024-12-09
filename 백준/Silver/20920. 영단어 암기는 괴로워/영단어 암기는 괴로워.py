from sys import stdin
from collections import Counter

# 자주 나오는 단어일수록 앞에 배치한다.
# 해당 단어의 길이가 길수록 앞에 배치한다.
# 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다.

n, m = map(int, stdin.readline().split())
mem = []

for _ in range(n):
    word = stdin.readline().split('\n')[0]
    if len(word)<m:
        continue
    mem.append(word)
counter = Counter(mem)
mem = sorted(counter.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for m in mem:
    print(m[0])