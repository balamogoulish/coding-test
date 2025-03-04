'''
n: 1~n까지 비밀코드로 가능한 숫자 범위
q: 시도한 숫자
ans: 시도한 숫자 중 비밀코드로 맞는 것

=> 비밀코드로 가능한 정수 조합 개수

combinations으로 가능한 숫자 조합(5개)를 모두 구하고, 특정 숫자 조합이 비밀코드라고 가정하여, ans와 일치하는 것의 개수를 찾는다.
1. combinations로 1~n까지의 수를 찾아 sort
2. 각 q[i]에서 비교하여 일치하는 개수가 ans[i]와 모두 같은 경우 answer+1

'''
from itertools import combinations

def is_compare_right(a, b, cnt):
    x = len(a)
    match_cnt = 0
    for i in range(x):
        if b[i] in a:
            match_cnt+=1
    if match_cnt==cnt:
        return True
    return False

def solution(n, q, ans):
    answer = 0
    numbers = [i for i in range(1, n+1)]
    m = len(q)
    secrets = combinations(numbers, 5)
    
    for secret in secrets:
        isAnswer = True
        # print(secret, '-----------------------------')
        for x in range(m):
            # print(secret, q[x], ans[x])
            if not is_compare_right(secret, q[x], ans[x]):
                isAnswer = False
                break
        if isAnswer:
            answer+=1

    
    # print(is_compare_right([1, 2, 3, 5, 8],[1, 2, 3, 4, 5],2))
    
    return answer