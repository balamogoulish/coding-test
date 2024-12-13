from sys import stdin
n = stdin.readline().split('\n')[0]
idx=0
for i in range(1, 1000000):
    for s in str(i):
        if n[idx]==s:
            idx+=1
            if idx>=len(n):
                print(i)
                exit()