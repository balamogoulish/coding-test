from sys import stdin

S = stdin.readline().strip()
x_num = 0
d_num = 0
answer = ''
for s in S:
    if s=='X': #X인 경우
        if x_num==0: #이전이 X가 아닌 경우, d_num만큼 .을 더함 
            answer += '.'*d_num
            d_num = 0
        x_num +=1
    else: #.인 경우
        if d_num==0: #이전이 .이 아닌 경우
            if x_num%2==0: #폴리오미노로 덮을 수 있는 경우
                answer+= 'AAAA'*(x_num//4)
                answer+= 'BB'*((x_num%4)//2)
                x_num = 0
            else: #폴리오미노로 덮을 수 없는 경우
                 print(-1)
                 exit()
        d_num += 1
if x_num==0: #이전이 X가 아닌 경우, d_num만큼 .을 더함 
    answer += '.'*d_num
    d_num = 0
if d_num==0: #이전이 .이 아닌 경우
    if x_num%2==0: #폴리오미노로 덮을 수 있는 경우
        answer+= 'AAAA'*(x_num//4)
        answer+= 'BB'*((x_num%4)//2)
        x_num = 0
    else: #폴리오미노로 덮을 수 없는 경우
        print(-1)
        exit()
print(answer)