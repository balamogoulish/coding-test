from sys import stdin
from collections import deque

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
ballons = deque([])
ans = ''
for i in range(n):
    ballons.append([i+1, arr[i]])

while len(ballons)>0:
    x = ballons.popleft()
    deleteNum = x[1]
    ans+=str(x[0])+' '
    if deleteNum > 0:
        deleteNum=-deleteNum+1
        ballons.rotate(deleteNum)
        # print('좌', deleteNum, ballons)
    else:
        ballons.rotate(-deleteNum)
        # print('우', deleteNum, ballons)
print(ans)