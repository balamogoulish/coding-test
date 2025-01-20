'''
while문 반복 시작
지금 시간에 요청 들어온 작업 있으면 꺼내서 우선순위 큐에 삽입
작업이 없을 경우 우선순위 큐로부터 작업을 받아온다.
우선순위 큐'와' jobs 배열에 있는 작업을 전부 처리했을 경우에만 작업 중단
시간 경과
작업 진행중일 경우 작업 진행시간을 체크하고, 작업 완료되었을 경우 현재 작업을 비우고 걸린 시간을 기록
2번으로
'''
from collections import deque
import heapq

def solution(jobs):
    curr_t = 0 #경과 시간
    work_t = 0 #작업 시간
    q = [] #우선 순위 큐
    job_list = deque(sorted([[jobs[i][0], jobs[i][1], i] for i in range(len(jobs))])) #요청 시간, 소요 시간, 작업 번호
    
    while len(q)>0 or len(job_list)>0: #우선 순위 큐와 작업 리스트를 전부 처리한 경우 중단
        #현재 시간에 요청 들어온 작업이 있으면 꺼내서 우선순위 큐에 삽입
        while len(job_list)>0 and job_list[0][0]<=curr_t:
            s, l, n = job_list.popleft()
            heapq.heappush(q, [l, s, n])
        if q:
            l, s, n = heapq.heappop(q)
            curr_t+=l
            work_t+=curr_t-s
        else:
            curr_t+=1
    return work_t//len(jobs)