from sys import stdin

n, k = map(int, stdin.readline().split())

left = 1
right = (n+2)//2

while left<=right:
    mid = (left+right)//2
    if mid*(n+2-mid)==k:
        print('YES')
        exit()
    elif mid*(n+2-mid)>k: #작아져야 함
        right = mid-1
    else:
        left = mid+1
print('NO')
        