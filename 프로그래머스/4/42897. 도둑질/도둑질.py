'''
연속된 인덱스에 접근하면 안됨.
이때 money의 최댓값은?

1. 처음 집을 털 때 => 인덱스 0을 털었을 때, len(money)-1은 털 수 없음
2. 처음 집을 털지 않을 때len(money)-1을 털었을 때, 0을 털 수 없음



'''

def solution(money):

    n = len(money)

    # 첫번째 집을 선택했을 때, 마지막 집은 더해주면 안된다.
    dp = [0 for _ in range(n)]
    dp[0] = money[0]
    dp[1] = money[1]
    dp[2] = money[2] + money[0]

    for i in range(3, n):
        # i 번째의 최대값은, i-2, i-3 번째 중 큰 값을 택하고, 자신의 값을 더하기 
        dp[i] = max(dp[i-2], dp[i-3]) + money[i]

    max_1 = max(dp[:-1])



    # 첫번째 집을 선택하지 않았을 때, 마지막 집은 더해줘도 된다.     
    dp = [0 for _ in range(n)]
    dp[0] = 0    
    dp[1] = money[1]
    dp[2] = money[2]

    for i in range(3, n):
        dp[i] = max(dp[i-2], dp[i-3]) + money[i]

    max_2 = max(dp)        


    return max(max_1, max_2)