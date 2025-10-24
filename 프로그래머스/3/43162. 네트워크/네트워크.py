'''
영역 개수 구하기 문제
    answer = 0
    
    visited = [False for _ in range(n)]
    
    def dfs(curr):
        for nxt in range(n):
            if computers[curr][nxt]==1 and not visited[nxt]:
                visited[nxt] = True
                dfs(nxt)
    
    for curr in range(n):
        if not visited[curr]:
            answer+=1
            visited[curr] = True
            dfs(curr)
    
    return answer
'''

def solution(n, computers):
    answer = 0
    
    visited = [False for _ in range(n)];
    
    def dfs(curr):
        for nxt in range(n):
            if computers[curr][nxt]==1 and not visited[nxt]:
                visited[nxt] = True
                dfs(nxt)
    
    for curr in range(n):
        if not visited[curr]:
            answer+=1
            dfs(curr)
    
    return answer
    
    
