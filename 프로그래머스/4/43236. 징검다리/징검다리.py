'''
출발지점 - 0
도착지점 - distance
바위를 n개 제거했을 때 출발지점, 바위들, 도착 지점 간의 거리의 최솟값들의 최댓값

이분탐색 방식으로 풀 때
1. 가능한 답의 최소, 최대는 0, distance
2. 순차적으로 거리를 계산했을 때, mid보다 보다 작으면 현재 바위를 제거하고

[0, 2, 11, 14, 17, 21, 25]3
12 => 0 0 0 14 14 
'''

def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    if 0 not in rocks:
        rocks.append(0)
    if distance not in rocks:
        rocks.append(distance)
    
    rocks.sort()
    
    while start<=end:
        mid = (start+end)//2
        cnt = 0
        tmp = [r for r in rocks]

        for i in range(1, len(rocks)):
            if tmp[i]-tmp[i-1] < mid: #지점 간의 거리가 mid보다 작으면 이전 바위 위치를 현재 바위 위치로 바꿈 cnt+1
                cnt+=1
                tmp[i] = tmp[i-1]
            if cnt>n:
                break
        if cnt>n:
            end = mid-1
        else:
            answer = mid
            start = mid+1
    
    return answer