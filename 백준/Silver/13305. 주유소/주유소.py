# 싼 주유소가 나오기 전까지의 거리는 현재 주유소에서 채우고 가야 함
from sys import stdin

n = int(stdin.readline())
d_arr = list(map(int, stdin.readline().split()))
c_arr = list(map(int, stdin.readline().split()))

cheap_arr = []
ans =0

# 뒤에 더 싼 주유소가 있으면 해당 주유소 index를 넣고, 없으면 -1을 넣음
for i in range(n-1):
    x=-1
    for j in range(i+1, n-1):
        if c_arr[i]>c_arr[j]:
            x=j
            break
    cheap_arr.append(x)

i = 0
while i!=(n-1):
    if cheap_arr[i]==-1:
        ans+=sum(d_arr[i:])*c_arr[i]
        print(ans)
        break
    else:
        ans+=sum(d_arr[i:cheap_arr[i]])*c_arr[i]
    i=cheap_arr[i]