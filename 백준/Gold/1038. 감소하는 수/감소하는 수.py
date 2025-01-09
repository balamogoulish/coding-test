from sys import stdin

n = int(stdin.readline())
decrease_num = []


'''
#한 자리인 경우 : 1~9 => 1+1+1+.. => 9
#두 자리인 경우 : 10, 20, 21, 30, 31, 32, ... => 1+ 2+ 3+ 4+ 5+ 6+ 7+ 8+ 9 => 45
#세 자리인 경우 : 
    210, => 1
    310, 320, 321, => 1+2 
    410, 420, 421, 430, 431, 432, => 1+2+3 
    510, 520, 521, 530, 531, 532, 540, 541, 542, 543 => 1+2+3+4

1. 가장 큰 자릿수 하나를 선택함 => a0
2. 그 다음 자릿수는 a0보다 작음 => a1
3. 2번을 반복
'''

def decrease(x):
    decrease_num.append(x)
    if x< 100000000000000000000000:
        for i in range(int(str(x)[-1])):
            decrease(int(str(x)+str(i)))
for i in range(10):
    decrease(i)
decrease_num.sort()
if n>1022:
    print(-1)
else:
    print(decrease_num[n])
