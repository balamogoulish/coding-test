'''
n: 총 지역수
roads: 두 지역을 왕복할 수 있는 길 배열
sources: 각 부대원이 위치한 지역
destination: 강철부대 지역

시작을 destination에서 해서 각각의 node에 대한 최단 경로를 입력하자!
'''
from collections import deque

def solution(n, roads, sources, destination):
    answer = [-1 for _ in range(n+1)]
    nodes = {} #node[x] = [x와 연결된 요소]
    
    #node 초기 값 세팅
    for road in roads:
        x, y = road
        if x not in nodes:
            nodes[x] = []
        if y not in nodes:
            nodes[y] = []
        nodes[x].append(y)
        nodes[y].append(x)

    def bfs():
        dq = deque([[destination, 0]])
        answer[destination] = 0
        reached_cnt = len(sources)
        
        while dq:
            curr, cnt = dq.popleft()
            if curr not in nodes:
                continue
            for nxt in nodes[curr]:
                if answer[nxt]!=-1:
                    continue
                answer[nxt] = cnt+1
                dq.append([nxt, cnt+1])
                if nxt in sources:
                    reached_cnt-=1
                    if reached_cnt==0:
                        break
    bfs()
    result = []
    for source in sources:
        result.append(answer[source])
                    

    
    
    return result