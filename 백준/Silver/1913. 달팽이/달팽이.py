from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
snail = [[0]*n for _ in range(n)]
answer = ''
# 가운데 1 채우기
x, y =n//2, n//2
snail[x][y] = 1

for i in range(3, n+1, 2):
    t, b, l, r = i-1, i-1, i-1, i-2
    x-=1
    snail[x][y] = ((i-2)**2)+1
    for j in range(((i-2)**2)+2, i**2+1):
        if r>0:
            r-=1
            y+=1
        elif b>0:
            b-=1
            x+=1
        elif l>0:
            l-=1
            y-=1
        elif t>0:
            t-=1
            x-=1
        snail[x][y]=j
for i in range(n):
    for j in range(n):
        if snail[i][j]==m: 
            answer=str(i+1)+' '+str(j+1)
        print(snail[i][j], end=' ')
    print()
print(answer)
    