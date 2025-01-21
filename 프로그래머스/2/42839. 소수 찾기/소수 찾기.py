from itertools import permutations

def isPrime(x):
    if x in [0, 1]:
        return False
    if x == 2:
        return True
    
    for i in range(2, int(x**(0.5)+1)):
        if x%i==0:
            return False
    return True

def solution(numbers):
    answer = set([])
    
    for i in range(1, len(numbers)+1):
        perm = (permutations(numbers, i))
        for p in set(perm):
            num = int(''.join(p))
            if isPrime(num):
                answer.add(num)
    
    return len(answer)



    