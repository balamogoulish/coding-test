from sys import stdin

n = int(stdin.readline())
hp = []
for i in range(n):
    x = list(map(int, stdin.readline().split()))
    hp+=(x)
    hp = sorted(hp, reverse= True)
    hp = hp[:n]
    
print(hp[n-1])