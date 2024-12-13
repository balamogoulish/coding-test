from sys import stdin
from collections import Counter

name = Counter(stdin.readline().split('\n')[0])
answer = ''
mid = ''
result = ''

for i in range(65, 91):
    alphabet = chr(i)
    cnt = name[alphabet]
    
    if cnt%2!=0: # 알파벳이 홀수 개인 경우
        # print('홀수:', alphabet, cnt)
        cnt-=1
        if mid=='': #홀수 개의 알파벳이 처음인 경우
            mid = alphabet
        else:
            answer = "I'm Sorry Hansoo"
            break
    if cnt%2==0: # 알파벳이 짝수 개인 경우
        answer+=alphabet*(cnt//2)
        # print('짝수:', alphabet, cnt)
if answer != "I'm Sorry Hansoo":
    result = answer+mid
    for i in range(len(answer)):
        result+=answer[len(answer)-i-1]
    print(result)
else:
    print(answer)
