# [최소 필요 피로도, 소모 피로도]
# 최소 필요 피로도 >= 소모 피로도
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    dungeons = permutations(dungeons, len(dungeons))
    
    for dungeon in dungeons:
        cnt = 0
        tired = k
        for d in dungeon:
            limit, pay = d
            if tired>=limit:
                tired-=pay
                cnt+=1
        answer = max(cnt, answer)

    return answer