from sys import stdin
from collections import Counter

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    m = list(map(int, stdin.readline().split(' ')))
    m = [x for x in m if m.count(x)>=6]
    
    race = [[] for i in range(n)]
    for i in range(len(m)):
        race[m[i]-1].append(i+1)
    min_s = 1000000
    ans = 0
    five = 0
    for j in range(n):
        if len(race[j])>=6:
            race[j].sort()
            if min_s > sum(race[j][:4]):
                ans = j+1
                min_s = sum(race[j][:4])
                five = race[j][4]
            elif min_s == sum(race[j][:4]) and five>race[j][4]:
                ans = j+1
                min_s = sum(race[j][:4])
                five = race[j][4]
    print(ans)
   