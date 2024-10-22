#https://www.acmicpc.net/problem/4673

#셀프 넘버가 아닌 수를 담는 배열 선언
non_self = [] 

for x in range(0, 10000):
    for a in str(x): #x = 자기 자신 + 각 자리의 수의 합
        x+=int(a)
    non_self.append(x)

for i in range(0, 10000): #non_self 배열에 없는 수 출력
    if i not in non_self:
        print(i)
