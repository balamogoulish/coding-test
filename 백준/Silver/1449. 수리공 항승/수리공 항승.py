from sys import stdin

n, l = map(int, stdin.readline().split())
water = list(map(int, stdin.readline().split()))
water = sorted(water)
ans = 0
dist = 0
for i in range(1, n):
    dist+= water[i]-water[i-1]
    if dist+1>l: #이전 구멍들까지의 거리가 테이프보다 길면, 이전 구멍들을 막음
        ans+=1
        dist=0

print(ans+1)