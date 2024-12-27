from sys import stdin
import sys

sys.setrecursionlimit(10**6)

n = int(stdin.readline())
table = [int(stdin.readline()) for _ in range(n)]
visited = [False for _ in range(n)]
answer = set([])

tmp1 = [] #첫째 줄의 임시 배열
tmp2 = [] #둘째 줄의 임시 배열 

#연결된 영역을 찾아 첫 번째 줄과 두 번째 줄의 배열을 각각 만든 다음, 같으면 set 집합에 추가함 
def dfs(i):
    visited[i]=True
    a = i+1 #첫번째 줄
    b = table[i] #두번째 줄
    tmp1.append(a)
    tmp2.append(b)
    if not visited[b-1]:
        dfs(b-1)

for i in range(n):
    tmp1 = []
    tmp2 = []
    visited = [False for _ in range(n)]
    dfs(i)
    if sorted(tmp1) == sorted(tmp2):
        for t in tmp2:
            answer.add(t)
print(len(answer))
for a in sorted(answer):
    print(a)
    
# 1 2 3 4 5 6
# 2 3 2 5 6 5