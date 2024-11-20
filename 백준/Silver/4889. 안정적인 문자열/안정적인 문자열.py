from sys import stdin

for i in range(1000000000):
    strs = stdin.readline().split('\n')[0]
    cnt = 0
    stack = []
    
    if strs[0]=='-':
        break
    
    for s in strs:
        if s=='{':
            stack.append(s)
        
        if s=='}':
            if len(stack)==0:
                stack.append('{')
                cnt+=1
            else:
                prev = stack.pop()
                if prev!='{':
                    cnt+=1
    
    cnt += len(stack)//2
    print(str(i+1)+'. '+str(cnt))