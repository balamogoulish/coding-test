from itertools import product

def solution(word):
    answer = 0
    dic = []
    for i in range(1, 6):
        per = product(['A', 'E', 'I', 'O', 'U'], repeat=i)
        for p in per:
            tmp = ''
            for a in p:
                tmp+=a
            dic.append(tmp)
    dic = sorted(dic)
    
    for i in range(len(dic)):
        if word==dic[i]:
            return i+1
