from sys import stdin

while True:
    str_x = stdin.readline()
    temp = []
    
    if str_x[0]=='.': #종료 조건
        break
    
    ans = 'yes'
    for x in str_x:
        if x=='(' or x=='[':
            temp.append(x)
        elif x==')' or x==']':
            if len(temp)==0:
                ans = 'no'
                break
            a = temp.pop()
            if x==')' and a!='(':
                ans = 'no'
                break
            if x==']' and a!='[':
                ans = 'no'
                break
    if len(temp)!=0:
        ans='no'
    print(ans)