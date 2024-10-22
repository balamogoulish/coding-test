#https://www.acmicpc.net/problem/20365

n = int(input())
colors = input()
answer = 0

#R,B로 슬라이스
rb = []
x=1
for i in range(1, n):
    if(colors[i]==colors[i-1]):
        x+=1
    else:
        rb.append(x)
        x=1
rb.append(x)
print(len(rb)//2+1)
