from sys import stdin

def calculate(op, num1, num2):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*':
        return num1*num2
    else:
        return num1/num2

def solution():
    n = int(stdin.readline()) #피연산자 수
    postfix = stdin.readline().strip() #후위표기식
    stack = []
    nums = {}
    
    
    for x in postfix:
        if 65<=ord(x)<=90: #피연산지인 경우
            if x not in nums:
                nums[x]=int(stdin.readline())
            stack.append(nums[x])
        else: #연산자인 경우
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(calculate(x, num2, num1))
    return '{:.2f}'.format(stack[0])

print(solution())