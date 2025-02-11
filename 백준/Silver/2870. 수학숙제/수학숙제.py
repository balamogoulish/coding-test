'''
n: 알파벳 소문자+숫자 조합의 글자 줄 수
1. 숫자를 오름차순으로 정리. 앞 숫자가 0인 경우 생략 가능능

'''
from sys import stdin

n = int(stdin.readline())
numbers = []

for _ in range(n):
    words = stdin.readline().strip()
    number = ''
    
    for w in words:
        if w.isdigit():
            number+=w
        else:
            if len(number)>0:
                numbers.append(int(number))
                number = ''
    if len(number)>0:
        numbers.append(int(number))

numbers.sort()
for n in numbers:
    print(n)