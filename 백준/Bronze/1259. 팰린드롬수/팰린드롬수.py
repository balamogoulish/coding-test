from sys import stdin
from collections import deque

while True:
    arr = deque(stdin.readline())
    ans = 'yes'
    if arr[0]=='0':
        break
    
    for i in range(len(arr)//2):
        r = arr[i]
        l = arr[len(arr)-2-i]
        if r != l:
            ans = 'no'
            break
    print(ans)