'''
10 =5*2

0의 개수 = 5의 배수의 개수

6! = 1x2x3x4x5x6 => 0 1개
'''

from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    cnt = 0
    i = 5
    
    while i<=n:
        cnt+=n//i
        i*=5
    print(cnt)