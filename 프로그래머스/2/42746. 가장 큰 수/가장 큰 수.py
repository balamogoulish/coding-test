def solution(numbers):
    answer = ''.join(sorted([str(i) for i in numbers], key = lambda x : x*4, reverse = True))
    return answer if len(answer)!=answer.count('0') else '0'