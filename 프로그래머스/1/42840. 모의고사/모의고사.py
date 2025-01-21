def solution(answers):
    answer = []
    methods = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    result = []
    for i in range(3):
        score = 0
        method = methods[i]
        for j in range(len(answers)):
            if answers[j] == method[j%len(method)]:
                score+=1
        answer.append(score)
    
    for i in range(3):
        if max(answer)==answer[i]:
            result.append(i+1)
    return result