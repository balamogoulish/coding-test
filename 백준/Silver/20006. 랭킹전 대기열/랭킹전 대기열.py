from sys import stdin

p, m = map(int, stdin.readline().split())

players = []
rooms = []
for _ in range(p):
    l, n = map(str,stdin.readline().split())
    players.append([int(l), n])

for p in players:
    isRoom = False
    for i in range(len(rooms)):
        if rooms[i][0][0]+10>=p[0] and rooms[i][0][0]-10<=p[0] and len(rooms[i])<m: 
            isRoom = True
            rooms[i].append(p)
            break
    #가능한 방이 없는 경우 방 생성 후 들어가기
    if isRoom==False:
        rooms.append([p])
for r in rooms:
    if len(r)==m:
        print('Started!')
    else:
        print('Waiting!')
    ans = sorted(r, key=lambda x:x[1])
    for x in ans:
        print(x[0], x[1])