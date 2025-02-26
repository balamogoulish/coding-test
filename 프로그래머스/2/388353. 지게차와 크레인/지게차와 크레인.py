'''
1. 
'''
def is_outside(x, y, graph):
    dx,dy=[0,0,1,-1],[-1,1,0,0]
    # 내가 -1인 경우, 주변에 0이 있으면 -1으로 만들고 다시 반복
    if graph[y][x]==-1:
        for k in range(4):
            nx, ny= x+dx[k], y+dy[k]
            if graph[ny][nx]==0:
                graph[ny][nx] = -1
                is_outside(nx, ny, graph)
        
    # 내가 0인 경우, 주변에 -1이 있으면 날 -1으로 만들고 다시 반복
    else:
        for k in range(4):
            nx, ny= x+dx[k], y+dy[k]
            if graph[ny][nx]==-1:
                graph[y][x] = -1
                is_outside(x, y, graph)
                break
            

def move_outside_box(n, m, graph, target):
    boxes = []
    dx,dy=[0,0,1,-1],[-1,1,0,0]
    for y in range(1, n-1):
        for x in range(1, m-1):
            if graph[y][x]==target:
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if graph[ny][nx]==-1:
                        boxes.append([x, y])
                        break
    for box in boxes:
        x, y = box
        graph[y][x] = -1
        is_outside(x, y, graph)

def move_all(n, m, graph, target):
    for y in range(n):
        for x in range(m):
            if graph[y][x] == target:
                graph[y][x] = 0
                is_outside(x, y, graph)
                
def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    answer = (n+2)*(m+2)
    
    graph = [[-1 for _ in range(m+2)] for _ in range(n+2)]
    for y in range(n):
        for x in range(m):
            graph[y+1][x+1] = storage[y][x]
    
    for request in requests:
        if len(request)==1:
            move_outside_box(n+2, m+2, graph, request)
        else:
            move_all(n+2, m+2, graph, request[0])
    
    for row in graph:
        for c in row:
            if c==-1 or c==0:
                answer-=1
            
    return answer