from sys import stdin

n = int(stdin.readline())
d_arr = list(map(int, stdin.readline().split()))
c_arr = list(map(int, stdin.readline().split()))

min_cost= 1000000000
ans = 0
for i in range(n-1):
    if c_arr[i]<=min_cost:
        min_cost=c_arr[i]
    ans+=d_arr[i]*min_cost
print(ans)