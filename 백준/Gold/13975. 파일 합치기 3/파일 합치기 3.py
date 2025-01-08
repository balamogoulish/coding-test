from sys import stdin
import heapq

T = int(stdin.readline())

for _ in range(T):
    k = int(stdin.readline())
    files = sorted(list(map(int, stdin.readline().split())))
    answer = 0
    
    while files:
        c1, c2 = 0 , 0
        c1 = heapq.heappop(files)
        if files:
            c2 = heapq.heappop(files)
        else:
            break
        answer+=c1+c2
        heapq.heappush(files, c1+c2)
    print(answer)