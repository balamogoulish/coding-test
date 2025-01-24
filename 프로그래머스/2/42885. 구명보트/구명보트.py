#무거운 사람이 가벼운 사람과 가는 것이 좋다. 10 20 30
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    f=0
    b=1
    while f<len(people)-b:
        if(people[f]+people[len(people)-b] <= limit): #가장 무거운 사람+가장 가벼운 사람 <= limit
            b+=1
        answer+=1
        f+=1

    if(f==len(people)-b):
        answer+=1
    return answer