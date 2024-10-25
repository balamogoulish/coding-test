n = int(input())
a = n // 5 #5로 나눌 수 있는 최대 몫
valid = 0

for i in range(a+1): #i=0~a
    c = n-(5*(a-i))
    if(c%3 == 0): 
        print(a-i+(c//3))
        valid = 1
        break
if valid==0:
    print(-1)