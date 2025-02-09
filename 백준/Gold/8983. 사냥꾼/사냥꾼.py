'''
m: 사대 수 (1~100000)
n: 동물 수 (1~100000)
l: 사정거리 (1~1000,000,000)

m_list: 사대 위치(x 좌표) 배열


1. 사대 중 동물과 가장 가까운 사대와의 거리를 구함
2. 이 거리가 사정거리보다 가까우면 cnt 증가가

'''

from bisect import bisect_right, bisect_left
from sys import stdin

m,n,l = map(int, stdin.readline().split())
m_list = sorted(map(int, stdin.readline().split()))

cnt = 0

for _ in range(n):
    x, y = map(int, stdin.readline().split())
    i = bisect_right(m_list, x) #x보다 큰 첫 번째 원소의 인덱스 반환, 이때 i-1은 x와 같거나 작은 원소의 인덱스 
    dist = y #사대와 동물 간 거리의 최솟값
    
    dist+=min(abs(x-m_list[i%m]), abs(x-m_list[(i-1)%m]))
    if l>=dist:
        cnt+=1
    
print(cnt)

    