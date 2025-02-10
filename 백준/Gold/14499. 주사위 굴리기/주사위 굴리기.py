'''
n * m: 세로 x 가로
x y: 주사위를 놓은 곳의 좌표
graph: 지도

1. 현재 칸이 0인 경우,
    a. 주사위 바닥의 수가 칸에 복사됨
2. 현재 칸이 0이 아닌 경우, 
    a. 칸에 쓰여있는 수가 바닥에 복사됨
    b. 칸에 쓰여있는 수가 0이 됨
3. 주사위가 지도 바깥으로 이동해야 하는 경우 해당 명령을 무시, 출력 X
=> 주사위가 이동할 때마다 상단에 쓰여 있는 값을 출력

===주사위===
1이 윗면, 동쪽이 3인 경우
동쪽으로 이동하면 
    윗면이 동쪽이 됨: u=>e
    동쪽이 바닥이 됨: e=>d
    바닥이 서쪽이 됨: d=>w
    서쪽이 윗면이 됨: w=>u
서쪽으로 이동하면 동쪽과 반대로 이동
북쪽으로 이동하면
    윗면이 북쪽이 됨: u=>n
    북쪽이 바닥이 됨: n=>d
    바닥이 남쪽이 됨: d=>s
    남쪽이 윗면이 됨: s=>u
남쪽으로 이동하면 북쪽과 반대로 이동
'''
from sys import stdin

n, m, x, y, k = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
order = list(map(int, stdin.readline().split()))
dice = [0 for _ in range(6)] #[u, n, e, w, s, d] 

def moveWest():
    tmp = dice[0]
    dice[0] = dice[2]
    dice[2] = dice[5]
    dice[5] = dice[3]
    dice[3] = tmp

def moveEast():
    tmp = dice[2]
    dice[2] = dice[0]
    dice[0] = dice[3]
    dice[3] = dice[5]
    dice[5] = tmp
    
def moveNorth():
    tmp = dice[0]
    dice[0] = dice[4]
    dice[4] = dice[5]
    dice[5] = dice[1]
    dice[1] = tmp

def moveSouth():
    tmp = dice[0]
    dice[0] = dice[1]
    dice[1] = dice[5]
    dice[5] = dice[4]
    dice[4] = tmp

for o in order:
    #지도를 벗어나지 않는 경우, 주사위를 이동함 
    if o==1 and y+1<m: #동쪽으로 이동
        moveEast()
        y+=1
    elif o==2 and y-1>=0: #서쪽으로 이동
        moveWest()
        y-=1
    elif o==3 and x-1>=0: #북쪽으로 이동
        moveNorth()
        x-=1
    elif o==4 and x+1<n: #남쪽으로 이동
        moveSouth()
        x+=1
    else:
        continue
    
    if graph[x][y]==0:
        graph[x][y] = dice[5]
    else:
        dice[5] = graph[x][y]
        graph[x][y]=0
    print(dice[0])
