from sys import stdin
import heapq

n = int(stdin.readline())
hp = []

for _ in range(n):
    x = int(stdin.readline())
    if x == 0:
        if len(hp)==0:
            print(0)
        else:
            print(heapq.heappop(hp))
    else:
        heapq.heappush(hp, x)