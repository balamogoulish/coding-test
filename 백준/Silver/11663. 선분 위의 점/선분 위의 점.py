# 1. 점을 크기순으로 정렬
# 2. 시작점보다 크거나 같은 점 index1 탐색
# 3. 끝점보다 작거나 같은 index2 탐색
# 4. index2-index1+1 => 해당 선분 위의 점 

from sys import stdin

def find_min_dot(dots, start):
    s=0 #시작 인덱스 
    e=len(dots)-1 #끝 인덱스
    answer = e+1
    
    while s<=e:
        mid = (s+e)//2
        if dots[mid]>=start:
            answer=mid
            e=mid-1
        else:
            s=mid+1
    return answer
    
def find_max_dot(dots, last):
    s=0 #시작 인덱스 
    e=len(dots)-1 #끝 인덱스
    answer = -1
    
    while s<=e:
        mid =(s+e)//2
        if dots[mid]<=last:
            answer=mid
            s=mid+1
        else:
            e=mid-1
    return answer

def solution():
    n, m =map(int, stdin.readline().split())
    dots = sorted(list(map(int, stdin.readline().split())))
    cnt_dots = []
    
    for _ in range(m):
        cnt = 0
        line = list(map(int, stdin.readline().split()))
        min_index = find_min_dot(dots, line[0])
        max_index = find_max_dot(dots, line[1])
        cnt = max_index-min_index+1
        if cnt<0:
            cnt=0
        print(cnt)
        
solution()