from sys import stdin
from itertools import combinations

def permute(n,m):
    res = 1
    for i in range(m):
        res*=(n-i)
    return res

def solution():
    n, m =map(int, stdin.readline().split())
    
    p = permute(n, m)
    k_factorial = permute(m, m)
    
    print(str(int(p//k_factorial)))



solution()