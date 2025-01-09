from sys import stdin

'''
1. 피연산자는 그대로 출력
2. 연산자는 스택이 비어있으면 PUSH
3. STACK의 TOP이 자신보다 우선순위가 높거나 같다면 POP하고, 자신을 담음
4. 여는 괄호는 닫는 괄호가 아니면  POP하지 않음
5. 닫는 괄호가 나오면 여는 괄호가 나올 때까지 POP
6. 식이 끝나면 STACK을 차례로 POP
'''
order = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3, ')': 4}

infix = stdin.readline().strip()
stack = []
answer = ''

for i in infix:
    if i not in order: #피연산자인 경우 
        answer+=i
    else: #연산자인 경우
        if len(stack)==0: #스택이 비어있는 경우
            stack.append(i)
        elif i==')': #닫는 괄호의 경우
            while stack:
                x = stack.pop()
                if x=='(':
                    break
                answer+=x
        else: # 나머지의 경우 
            while stack:
                x= stack.pop()
                if order[i]<=order[x] and x!='(':
                    answer+=x
                else:
                    stack.append(x)
                    break
            stack.append(i)
while stack:
    answer+=stack.pop()
print(answer)
                    