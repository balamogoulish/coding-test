from sys import stdin

T = int(stdin.readline())

def turnRight(n, x): #시계 방향 회전 함수
    result = []
    for k in x:
        tmp = []
        for l in k:
            tmp.append(l)
        result.append(tmp)
    for i in range(n):
        #1. x의 주 대각선을 가운데 열로 옮김
        result[i][((n+1)//2)-1] = x[i][i]
        #2. 가운데 열은 x의 부대각선으로 옮김
        result[i][n-i-1] = x[i][((n+1)//2)-1]
        #3. x의 부대각선을 x의 가운데 행으로 옯김
        result[((n+1)//2)-1][i] = x[n-i-1][i]
        #4. x의 가운데 행을 x의 주 대각선으로 옮김
        result[i][i] = x[((n+1)//2)-1][i]
    return result
    
for _ in range(T):
    x = []
    n, d = map(int, stdin.readline().split())
    for _ in range(n):
        x.append(list(map(int, stdin.readline().split())))
    d = ((360+d)%360)//45
    for _ in range(d):
        x = turnRight(n, x)
    for ans in x:
        for a in ans:
            print(a, end=' ')
        print()