#https://www.acmicpc.net/problem/7568

n = int(input())
big = []
rank = [1]*n

for _ in range(n):
    w, h = map(int, input().split())
    big.append((w, h))

for i in range(len(big)):
    curr = big[i]
    for j in range(i+1, len(big)):
        oth = big[j]
        if curr[0]>oth[0] and curr[1]>oth[1]: #curr이 oth보다 덩치가 클 경우
            rank[j]+=1
        elif curr[0]<oth[0] and curr[1]<oth[1]: #curr이 oth보다 덩치가 작은 경우우
            rank[i]+=1

for r in rank:
    print(r, end=' ')
