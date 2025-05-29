# 포도주 잔 선택 시, 모두 마시고 원위치 
# 연속으로 있는 3잔 X 
# 가장 많은 양의 포도주를 먹을 수 있는 양

from sys import stdin

def solution():
    n = int(stdin.readline()) #포도주 잔 개수 
    wines = [int(stdin.readline()) for _ in range(n)]

    # DP 문제
    # dp[n]: n까지의 포도주가 주어졌을 때의 최댓값
    # 1. n열 포도주를 안 마시는 경우 => dp[n] = dp[n-1]
    # 2. n열 포도주를 마시는 경우
        # 2.1. OXO => dp[n] = dp[n-2]+wines[n]
        # 2.2. XOO => dp[n] = dp[n-3]+wines[n-1]+wines[n]
    
    dp = [0 for _ in range(n)]
    dp[0] = wines[0]
    
    if n==1:
        print(wines[0])
    elif n==2:
        print(wines[0]+wines[1])
    else:
        for i in range(1, n):
            dp[i] = max(dp[i-1], dp[i-2]+wines[i], dp[i-3]+wines[i-1]+wines[i])
        print(dp[n-1])
    
solution()