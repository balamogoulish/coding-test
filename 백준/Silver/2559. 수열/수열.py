'''
누적합 + 부분합 문제
1. 누적합 => s_arr[i] = arr[i-1]+s_arr[i-1]
2. 부분합 => i~j까지의 합: s_arr[j]-s_arr[i-1]
'''

from sys import stdin

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
s_arr = [0 for _ in range(n+1)]


#누적합 
for i in range(1, n+1):
    s_arr[i] = s_arr[i-1]+arr[i-1]

answer = -100*k
for j in range(k, n+1):
    answer = max(answer, s_arr[j]-s_arr[j-k])
print(answer)