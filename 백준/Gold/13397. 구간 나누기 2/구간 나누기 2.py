from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

def isValid(x): #구간 점수의 최댓값이 x일 때, 구간의 수가 m개 이하인가?
    cnt = 1
    max_a = arr[0]
    min_a = arr[0]
    for a in arr:
        max_a = max(max_a, a)
        min_a = min(min_a, a)
        
        if max_a-min_a > x:
            cnt+=1
            max_a = a
            min_a = a
    return cnt<=m

left = 0
right = max(arr)
answer = right

while left<=right:
    mid =(left+right)//2
    if isValid(mid):
        right = mid-1
        answer = min(answer, mid)
    else:
        left = mid+1
        
print(answer)