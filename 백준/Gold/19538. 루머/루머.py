from sys import stdin
from collections import deque

n = int(stdin.readline()) #전체 사람의 수 
people = [[] for _ in range(n+1)] #people[i]는 i번 사람 주변인들의 배열 (양방향)
answer = [-1 for _ in range(n+1)] #루머 유포자가 되는 시간
visited = [False for _ in range(n+1)] #방문 여부
rumor_cnt_near = [0 for _ in range(n+1)] #주변인 중 루머 유포자의 수

for i in range(1, n+1):
    x = list(map(int, stdin.readline().split()))
    for l in x:
        if l!=0:
            people[i].append(l)

m = int(stdin.readline()) #최초 유포자의 수 
rumor_q = deque(list(map(int, stdin.readline().split()))) #최초 유포자 배열
for f in rumor_q: #초기 루머 유포자 방문 처리 및 시간 처리
    answer[f] = 0
    visited[f] = True

i=1
while rumor_q:
    tmp = deque([])
    while rumor_q:
        curr = rumor_q.popleft()
        for near in people[curr]:
            rumor_cnt_near[near] += 1
        for nxt in people[curr]:
            if not visited[nxt] and rumor_cnt_near[nxt]>=len(people[nxt])/2:
                tmp.append(nxt)
                visited[nxt] = True
                answer[nxt] = i
    rumor_q = tmp
    i+=1
for i in range(1, n+1):
    print(answer[i], end=' ')