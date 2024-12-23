from sys import stdin
from collections import deque

st = []
n = int(stdin.readline())
arr = deque([i for i in range(1, n+1)])
ans = []

for _ in range(n):
    m = int(stdin.readline())
    if len(st)>0 and st[-1]==m:
        st.pop()
        ans.append('-')
        continue
    while True:
        if len(arr)==0:
            break
        else:
            k = arr.popleft()
            st.append(k)
            ans.append('+')
            if k==m:
                st.pop()
                ans.append('-')
                break
if len(arr)>0 or len(st)>0:
    print('NO')
else:
    for a in ans:
        print(a)