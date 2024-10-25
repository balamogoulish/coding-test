from collections import deque

a = deque()
n, k = input().split()

for i in range(int(n)):
    a.append(i+1)

answer =[]
while len(a)>0:
    for _ in range(int(k)-1):
        x = a.popleft()
        a.append(x)
    x = a.popleft()
    answer.append(x)

print('<'+str(answer)[1:-1]+'>')