from sys import stdin

n = int(stdin.readline())
cost = list(map(int, stdin.readline().split())) 

bnp = [n, 0] #준현의 현금, 보유 주식 수
tim = [n, 0] #성민의 현금, 보유 주식 수

inc = 0 #연속 상승일
dec = 0 #연속 하락일

for i in range(len(cost)):
    #준현
    bnp[1]+=bnp[0]//cost[i]
    bnp[0]-=(bnp[0]//cost[i])*cost[i]
    
    #성민
    if i!=0:
        prev = cost[i-1]
        if prev<cost[i]: #가격 상승
            inc+=1
            dec=0
            if inc>=3:
                tim[0]+=tim[1]*cost[i]
                tim[1]=0
        elif prev>cost[i]: #가격 하락
            dec+=1
            inc=0
            if dec>=3:
                tim[1]+=tim[0]//cost[i]
                tim[0]-=(tim[0]//cost[i])*cost[i]
        else:
            inc=0
            dec=0
b= bnp[0]+bnp[1]*cost[-1]
t= tim[0]+tim[1]*cost[-1]
if b>t:
    print('BNP')
elif b<t:
    print('TIMING')
else:
    print("SAMESAME")
    