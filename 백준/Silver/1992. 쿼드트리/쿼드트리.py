from sys import stdin

n = int(stdin.readline().strip())
video = [list(map(int, stdin.readline().strip())) for _ in range(n)]

# 현재 영역이 모두 0이거나 모두 1인지 확인하는 함수
def get_zip(graph, x, y, size):
    first = graph[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if graph[i][j] != first:
                return -1  # 섞여 있으면 -1 반환
    return first

# 쿼드 트리 압축을 수행하는 DFS 함수
def dfs(graph, x, y, size):
    ziped = get_zip(graph, x, y, size)
    
    if ziped != -1:  # 모두 0 또는 1이면 그대로 반환
        return str(ziped)
    
    # 4개의 영역으로 나누어 재귀 호출
    half = size // 2
    top_left = dfs(graph, x, y, half)
    top_right = dfs(graph, x + half, y, half)
    bottom_left = dfs(graph, x, y + half, half)
    bottom_right = dfs(graph, x + half, y + half, half)

    return f"({top_left}{top_right}{bottom_left}{bottom_right})"

# 결과 출력
print(dfs(video, 0, 0, n))
