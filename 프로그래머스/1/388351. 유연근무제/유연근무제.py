'''

'''

def cal_time(time):
    h = time//100
    m = time%100
    if m>59:
        h+=1
        m-=60
    if h>23:
        h=0
    return h*100+m

def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        limit = cal_time(schedules[i]+10)
        today = startday%8
        isNotLate=True
        # print('--------')
        for j in timelogs[i]:
            # print(today,i, j)
            if today<6: #평일에 
                if j>limit: #지각하면
                    isNotLate = False
                    break
            today = (today+1)
            if today==8:
                today=1
        if isNotLate:
            answer+=1
    
    return answer