from sys import stdin

n = int(stdin.readline()) #테스트케이스 수

for _ in range(n):
    m = int(stdin.readline()) #의상 수
    clothes = {}
    answer = 1
    
    for _ in range(m):
        c_type = stdin.readline().split()[1]
        if c_type not in clothes:
            clothes[c_type] = 0
        clothes[c_type]+=1
    for c in clothes.items():
        answer*=(c[1]+1)
    print(answer-1)