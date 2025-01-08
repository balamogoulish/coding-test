from sys import stdin

n = int(stdin.readline()) #센서의 수
k = int(stdin.readline()) #집중국의 수
sensors = sorted(list(map(int, stdin.readline().split())))
dist = []

for i in range(1, n):
    dist.append(sensors[i]-sensors[i-1])
    
dist = sorted(dist, reverse=True)
print(sum(dist[k-1:]))