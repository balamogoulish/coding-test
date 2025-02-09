'''
N: 집의 개수
C: 공유기 개수
homes = 집 위치 배열(정렬됨)
answer = 공유기 간 최소 거리의 최댓값

1. 공유기는 집에만 설치할 수 있음
2. 가장 인접한 공유기의 거리가 최대가 되도록 함

mid = 공유기간 최소 거리
left = 1
right = homes[-1]-homes[0]

'''
from sys import stdin

N, C = map(int, stdin.readline().split())
homes = sorted([int(stdin.readline()) for _ in range(N)])

left = 1
right = homes[-1]-homes[0]

answer = 1

# print(homes)

while left<=right:
    mid = (left+right)//2
    cnt = 1
    dist = 0
    
    # print(mid, "=============")
    
    for i in range(1, N):
        dist+= homes[i]-homes[i-1]
        if dist>=mid:
            cnt+=1
            # print(homes[i], homes[i-1], dist, cnt)
            dist=0
        
        if cnt>=C:
            break
    if cnt>=C: #설치해야 하는 공유기가 더 많으면, 최소 거리를 줄여야 함
        answer = max(mid, answer)
        left = mid+1
    else:
        right = mid-1
        

print(answer)
        
        
        
        