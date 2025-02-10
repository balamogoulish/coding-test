from sys import stdin

while True:
    try:
        n = int(stdin.readline())
    except Exception:
        break
    num =  0
    i = 1
    
    while True:
        num = num*10+1
        num%=n
        
        if num==0:
            print(i)
            break
        i+=1
        