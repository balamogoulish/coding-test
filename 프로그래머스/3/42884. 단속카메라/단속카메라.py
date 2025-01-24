#영역 구하기 문제

def solution(routes):
    answer = 0
    visited = [False for _ in range(len(routes))]
    routes = sorted(routes)
    
    def NumOfCar(x):
        visited[x] = True
        start = routes[x][0] #가장 최대 start
        end = routes[x][1] #가장 최소 end
        for i in range(len(routes)):
            nxt_start, nxt_end = routes[i]
            if not visited[i] and end>=nxt_start:
                end = min(nxt_end, end)
                start = max(nxt_start, start)
                visited[i] = True
    
    for i in range(len(routes)):
        if not visited[i]: #아직 단속 카메라를 만난 적이 없는 경우
            answer+=1
            NumOfCar(i)
    
    return answer