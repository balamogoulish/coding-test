'''
screen_length: 스크린의 가로 길이
basket_length: 바구니의 길이
초기 바구니 위치: 1~m
바구니 위치: basket_start ~ basket_end=basket_start+basket_length

떨어지는 위치 x에 대해서
1. basket_start<=x<=basket_end이면 
    움직이지 않음
2. 밖인 경우
    x<basket_start인 경우 basket_start-x만큼 왼쪽으로 이동
    x>basket_end인 경우 x-basket_end만큼 오른쪽으로 이동

'''
from sys import stdin

screen_length, basket_length = map(int, stdin.readline().split())
j = int(stdin.readline())

move_cnt = 0
basket_start = 1
basket_end = basket_start+basket_length-1

for _ in range(j):
    apple_location = int(stdin.readline())
    
    if basket_start > apple_location:
        move_cnt+=basket_start-apple_location
        basket_start = apple_location
        basket_end = basket_start+basket_length-1
        
    if basket_end < apple_location:
        move_cnt+=apple_location-basket_end
        basket_end = apple_location
        basket_start = basket_end-basket_length+1
    
print(move_cnt)
        
