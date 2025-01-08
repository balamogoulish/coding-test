from sys import stdin
from collections import deque
import heapq

n = int(stdin.readline())

# 회의 시작 시간 기준으로 정렬
meets = deque(sorted([list(map(int, stdin.readline().split())) for _ in range(n)], key=lambda x: (x[0], x[1])))
rooms = []
heapq.heappush(rooms, meets.popleft()[1])

while meets:
    curr_start, curr_end = meets.popleft()
    min_end = heapq.heappop(rooms)
    
    if curr_start >= min_end:
        # 기존 방을 재활용: 가장 빨리 끝나는 방에 새로운 회의 배정
        heapq.heappush(rooms, curr_end)
    else:
        # 새로운 방이 필요: 기존 끝나는 시간(min_end)을 다시 넣고, 새로운 끝나는 시간 추가
        heapq.heappush(rooms, min_end)
        heapq.heappush(rooms, curr_end)

print(len(rooms))
