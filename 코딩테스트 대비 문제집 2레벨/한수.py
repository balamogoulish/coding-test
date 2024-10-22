#https://www.acmicpc.net/problem/1065
n = int(input())
ans =0 #한수가 아닌 수의 개수

for i in range(1, n+1):
    str_i = str(i) #각 자리수 별로 계산하기 위해 문자열 타입으로 변환
    diff = 0
    for j in range(1, len(str_i)):
        if j == 0: #첫 번째 자리에서는 diff가 없기 때문에 skip
            continue
        elif j==1: #두 번째 - 첫 번째 수 => diff
            diff = int(str_i[j])-int(str_i[j-1])
        else: 
            if diff != int(str_i[j])-int(str_i[j-1]): #diff와 수의 차이가 다른 경우 => 한수 X
                ans+=1
                break
print(n-ans)
