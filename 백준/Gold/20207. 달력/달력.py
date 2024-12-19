from sys import stdin

n = int(stdin.readline())
cal = [0 for _ in range(366)]
events = [list(map(int, stdin.readline().split())) for _ in range(n)]
answer = 0

for e in events:
    start = e[0]
    end = e[1]
    for d in range(start, end+1):
        cal[d]+=1

max_events = 0
cont = 0
for c in cal:
    if c==0: #일정이 없으면
        answer += max_events*cont
        max_events = 0
        cont = 0
    else:
        max_events = max(max_events, c)
        cont+=1
print(answer+max_events*cont)
