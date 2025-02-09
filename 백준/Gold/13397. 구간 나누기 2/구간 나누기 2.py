'''
n: 배열에 포함된 수의 개수
m: 팀 수

n을 m개의 팀으로 나눠야 함
구간 점수의 최댓값을 최소로 만듦 => answer
구간 점수 = 구간 내 최댓값-구간 내 최솟값

'''
from sys import stdin
from bisect import bisect_left, bisect_right

n, m = map(int, stdin.readline().split())
n_list = list(map(int, stdin.readline().split()))

left = 0
right = max(n_list)-min(n_list)

answer = right

while left<=right:
    mid = (left+right)//2 #구간 점수의 최댓값 
    cnt = 1 #구간의 수
    start_i = 0 #구간의 시작 지점
    for i in range(1, n+1):
        if max(n_list[start_i: i])-min(n_list[start_i: i ])>mid: 
            #구간 점수가 설정한 값보다 크면, 마지막 요소를 포함하지 않게 구간을 나눠야 함 
            start_i = i-1
            cnt+=1
            if cnt > m: #구간의 수가 가능한 수보다 크면 mid를 키워야 함
                break
    if cnt>m: 
        left=mid+1
    elif cnt<=m: # 구간의 수가 가능한 수보다 작으면 mid를 줄여도 됨
        answer = min(answer, mid)
        right=mid-1
            
print(answer)
            
            