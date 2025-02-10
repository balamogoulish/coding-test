'''
n: 재료 개수
m: 필요한 수
arr: 재료 번호 배열
'''

from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
arr = sorted(list(map(int, stdin.readline().split())))
answer = 0

start = 0
end = n-1

while start<end:
    if arr[start]+arr[end]==m:
        answer+=1
        start+=1
        end-=1
    elif arr[start]+arr[end]<m: #start를 증가시킴 
        start+=1
    else:
        end-=1

print(answer)