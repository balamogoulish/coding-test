'''
조건
- 여러 개의 소문자와 하나의 별표
- 

1. *를 중심으로 문자열을 자른다.
2. 앞, 뒤에서 각각의 문자를 검사해서 맞으면 DA, 틀리면 NE
'''

from sys import stdin

n = int(stdin.readline())
pattern = stdin.readline().strip().split("*")

for _ in range(n):
    file = stdin.readline().strip()
    if len(file) < len(pattern[0])+len(pattern[1]):
        print("NE")
        continue
    
    if file[:len(pattern[0])] != pattern[0] or file[len(file)-len(pattern[1]): ]!=pattern[1]:
        print("NE")
        continue
    print("DA")
    
    
    