from sys import stdin
import sys

sys.setrecursionlimit(10**6)

n, m, p =map(int, stdin.readline().split()) #n:노인의 수, m: 채널 수, p: 초기 채널
like = [] #나이가 어린 순
hate = {}
visited = [0 for _ in range(m+1)]
answer = [0] #채널을 바꾼 횟수 

for i in range(n):
    l, h = map(int, stdin.readline().split())
    if h not in hate:
        hate[h]=[]
    hate[h].append(i)
    like.append(l)

def changeCh(curr):
    if visited[curr]==1:
        print(-1)
    elif curr in hate:
        visited[curr] = 1
        answer[0]+=1
        person = min(hate[curr])
        changeCh(like[person])
    else:
        print(answer[0])

changeCh(p)