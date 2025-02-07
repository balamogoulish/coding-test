'''
answer[y][x]: [x, y]를 갈 수 있는 경우의 수
1. 갈 수 있는 경우의 수를 구하는 법
    - 네방향으로 answer[ny][nx]+=answer[y][x] 자기 자신을 더하면 됨
    - 단, nx, ny가 puddles에 있으면 안됨
'''


def solution(m, n, puddles):
    answer = [[0 for _ in range(m)] for _ in range(n)]
    answer[0][0] = 1 #처음 시작 지점에 도달할 수 있는 방법은 한 개
    
    dx, dy = [1, 0], [0, 1] #오른쪽, 위쪽
    
    for y in range(n):
        for x in range(m):
            for i in range(2):
                nx, ny = x+dx[i], y+dy[i]
                if [nx+1, ny+1] not in puddles and 0<=nx<m and 0<=ny<n:
                    answer[ny][nx]+=answer[y][x]
    
    for a in answer:
        print(a)
    
    return answer[n-1][m-1]%1000000007