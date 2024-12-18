from sys import stdin

n = int(stdin.readline())
rem = list(map(int, stdin.readline().split()))
ans = [100]*n

# 첫 번째 요소부터 순차적으로 계산
# 이미 요소가 있는 경우는 카운트하지 않고 다음 칸으로 넘어감
for i in range(n):
    cnt = rem[i]
    now = 0
    while cnt>0:
        if ans[now]>i+1: #키가 i+1인 사람보다 키가 크면 키가 큰 사람을 카운트함
            cnt-=1
        now+=1
    while ans[now]!=100:
        now+=1
    ans[now]=i+1
for a in ans:
    print(a, end=' ')