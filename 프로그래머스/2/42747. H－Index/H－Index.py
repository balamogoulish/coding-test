from collections import deque
def solution(citations):
    answer = 0
    citations = deque(sorted(citations))
    
    print(citations)
    h = 0
    while citations:
        while True:
            if len(citations)>0 and citations[0]<h:
                citations.popleft()
            else:
                break
        if len(citations)>0 and h<=citations[0]: #h번 이상 인용된 논문이 존재하는 경우
            if len(citations)>=h: #h번 이상 인용된 논문이 h편 이상인 경우
                answer = h
                h+=1
            else: #h번 이상 인용된 논문이 h편 미만인 경우
                break
    return answer