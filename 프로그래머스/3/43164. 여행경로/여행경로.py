'''
모든 경로 탐색 문제
모든 경로를 구한 후, 알파벳 순으로 가장 우선한 한 개의 경로를 return함

노드 문제로 전환하자! => start: [end, ...]
'''
from collections import deque

def solution(tickets):
    answer = []
    node = {}
    dq = deque() # [현재 공항, [tickets_index]]
    
    
    # node[start] = [end, ...] 로 변환
    for i in range(len(tickets)):
        start, end = tickets[i]
        if start not in node:
            node[start] = []
        node[start].append(i)
    
    
    # bfs로 풀어보자...
    dq.append(["ICN", []])
    while dq:
        curr, visited = dq.popleft()

        if len(visited)==len(tickets): #항공권을 모두 사용한 경우, answer에 경로 추가
            tmp = [tickets[i][0] for i in visited]
            tmp.append(tickets[visited[-1]][1])
            answer.append(tmp)
        if curr not in node: #curr에서 출발하는 항공권이 없는 경우, 그냥 다음으로 가자
            continue
        
        for nxt in node[curr]:
            if nxt not in visited: #curr에서 출발하는 항공권 중 사용하지 않은 항공권을 dq에 추가
                tmp_visited = [v for v in visited]
                tmp_visited.append(nxt)
                dq.append([tickets[nxt][1], tmp_visited])
    
    answer = sorted(answer)
    
    return answer[0]