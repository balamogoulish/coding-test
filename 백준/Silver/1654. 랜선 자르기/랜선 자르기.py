'''
K: 초기 전선 개수
N: 최종 길이가 같은 전선 개수

N보다 크거나 같은 수를 만들 수 있는 최대 길이는?
'''

from sys import stdin

k, n = map(int, stdin.readline().split())
lines = [int(stdin.readline()) for _ in range(k)]

min_l = 1 #최소 전선 길이
max_l = max(lines) #최대 전선 길이

def avail_line_num(l): #길이를 l이 되게 잘랐을 경우, 나오는 길이가 같은 전선의 수
    avail_cnt = 0
    for line in lines:
        avail_cnt+=line//l
    return avail_cnt

def find_longest_length(min_l, max_l):
    ans = 0
    while True:
        mid = (min_l+max_l)//2
        mid_cnt = avail_line_num(mid)
        
        if mid_cnt >= n: #가능한 전선 수가 n보다 크거나 같으면 -> mid를 더 키워보자! 
            min_l = mid+1
            ans = max(ans, mid)
        else: #가능한 전선 수가 n보다 작으면 -> mid를 줄이자!
            max_l = mid-1
        
        if max_l < min_l:
            return ans

print(find_longest_length(min_l, max_l))
    