from sys import stdin
from collections import deque

n = int(stdin.readline())
milks = sorted([int(stdin.readline()) for _ in range(n)], reverse=True)
m_q = deque(milks)
answer = 0

#2+1으로 최소 비용으로 사기 위해서는 비싼 거 두 개, 싼 거 한 개를 사야 함
while(n//3 >0):
    x, y, z= m_q.popleft(), m_q.popleft(), m_q.popleft()
    answer+=x+y
    n-=3
answer+=sum(m_q)
print(answer)
