from sys import stdin

h, w = map(int, stdin.readline().split())
block = list(map(int, stdin.readline().split()))
matrix = [[0 for _ in range(w)] for _ in range(h)]
answer = 0

for i in range(w):
    for j in range(h):
        if j<block[i]:
            matrix[h-j-1][i]=1
# 양옆이 막혀있으면 넓이에 포함
for i in range(h):
    isLeft = False
    cnt = 0
    
    for j in range(w):
        if matrix[i][j]==1 and isLeft==False: #왼쪽이 막혀있자 않은 상태에서 블록을 만나면
            #왼쪽이 막혀있다고 선언
            isLeft = True
        elif matrix[i][j]==1 and isLeft==True: #왼쪽이 막혀있고 블록을 만나면
            if cnt!=0: #사이에 빈 칸이 있는 경우
                answer+=cnt
                cnt=0
        elif matrix[i][j]==0 and isLeft==True: #왼쪽이 막혀있고 빈칸을 만나면
            cnt+=1
print(answer)
            
        

