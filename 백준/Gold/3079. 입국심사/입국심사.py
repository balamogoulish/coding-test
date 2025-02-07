'''
M: 인원 수
N: 심사대 수
T[k]: index가 k인 심사관의 심사 소요 시간

걸리는 최소 심사 시간: 0
걸리는 최대 심사 시간: 가장 심사 시간이 긴 사람한테만 받기기
'''

from sys import stdin

N, M = map(int, stdin.readline().split())
tests = [int(stdin.readline()) for _ in range(N)]

left = 0
right = max(tests)*M

answer = right

while left<=right:
    mid = (left+right)//2
    cnt = 0
    for t in tests:
        cnt += mid//t
        
        if cnt>=M: #가능한 인원이 같거나 많다면 시간을 줄여도 됨
            break
    if cnt>=M:
        right = mid-1
        answer = min(answer, mid)
    else:
        left = mid+1
print(answer)