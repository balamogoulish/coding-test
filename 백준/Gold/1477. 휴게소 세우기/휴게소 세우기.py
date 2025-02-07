'''
N: 휴게소의 개수
M: 더 지을 휴게소의 개수
L: 고속도로 길이이

휴게소 간 거리의 최댓값을 최소가 되도록 휴게소를 더 지을 때, 이때의 최대 거리

최대 거리를 mid로 두고 이분탐색을 진행함
1. i와 i-1의 거리가 mid보다 큰 경우, (rests[i]-rests[i-1])//mid, 
    나머지가 있는 경우 +1 만큼의 휴게소를 짓는다
2. 지은 휴게소의 개수가 M보다 크거나 같다면 mid를 줄인다.
3. 지은 휴게소의 개수가 M보다 작거나 같다면 일단 answer로 설정해두고 mid를 키운다.

'''
from sys import stdin

N, M, L = map(int, stdin.readline().split())
rests = list(map(int, stdin.readline().split()))
rests.append(0)
rests.append(L)
rests.sort()

left = 1
right = L

answer = L

while left<=right:
    
    mid = (left+right)//2
    cnt = 0
    for i in range(1, len(rests)):
        if rests[i]-rests[i-1] > mid:
            cnt=cnt+ ((rests[i]-rests[i-1])//mid) -1
            if (rests[i]-rests[i-1])%mid != 0:
                cnt+=1 
    if cnt<=M: #간격을 줄이자 
        right = mid-1
        answer = min(mid, answer)
    else: #필요한 휴게소가 가능한 휴게소보다 작으면 간격을 늘려도 된다.
        left = mid+1

print(answer)
            