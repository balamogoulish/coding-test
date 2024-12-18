from sys import stdin

n = int(stdin.readline()) #골이 들어간 횟수
goals = []
score = [0, 0] # 1팀:2팀
time = [[0,0], [0,0]]
last_time = [0, 0] # 마지막으로 득점한 시간
last_win = 0 # 마지막으로 이기고 있는 팀 => 0: 동점, 1: 1팀, 2: 2팀팀

for _ in range(n):
    team_num, t = map(str, stdin.readline().strip().split(' '))
    team_num = int(team_num)
    m, s = map(int, t.split(':'))
    goals.append([team_num, m, s])
goals =sorted(goals, key=lambda x: (x[1], x[2]))


for g in goals:
    team, m, s = g
    score[team-1]+=1 # 득점 처리
    if team==1 and score[0]>score[1] and last_win==0: #1팀이 역전한 경우
        last_time = [m, s]
        last_win = team
        
    elif team==2 and score[0]<score[1] and last_win==0: #2팀이 역전한 경우
        last_time = [m, s]
        last_win = team
        
        
    elif score[0]==score[1]: #동점이 된 경우
        # 이전에 이기고 있던 팀에 대해서 이기고 있는 시간을 더함
        sec = s-last_time[1]
        minute = m-last_time[0]
        if sec<0:
            sec = 60+sec
            minute-=1
        time[last_win-1][0]+=minute
        time[last_win-1][1]+=sec
        # last_time, last_win 갱신
        last_win = 0
        last_time = [minute, sec]
if last_win!=0:
    sec = 0-last_time[1]
    minute = 48-last_time[0]
    if sec<0:
        sec = 60+sec
        minute-=1
    time[last_win-1][0]+=minute
    time[last_win-1][1]+=sec
# 시간 정규화
for i in range(2):
    time[i][0] += time[i][1] // 60
    time[i][1] %= 60
# 출력
for t in time:
    print(f'{t[0]:02}:{t[1]:02}')
        