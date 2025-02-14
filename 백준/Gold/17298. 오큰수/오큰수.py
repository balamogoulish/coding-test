from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
answer = []
stack = []

while arr:
    curr = arr.pop()
    if len(stack)==0:
        stack.append(curr)
        answer.append(-1)
    else:
        if stack[-1]<=curr: 
            while len(stack)>0 and stack[-1]<=curr:
                stack.pop()
        
        if len(stack) == 0:
            answer.append(-1)
        else:
            answer.append(stack[-1])
        
        stack.append(curr)

for i in range(n):
    print(answer[n-i-1], end=' ')