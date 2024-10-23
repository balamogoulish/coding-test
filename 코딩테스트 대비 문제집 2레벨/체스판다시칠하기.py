#https://www.acmicpc.net/problem/1018

n, m = map(int, input().split())
board = []
ans = 64

#board에 각 문자를 2차원 배열로 입력하기기
for _ in range(n):
    board.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        b_ans = 0 #black으로 시작하는 경우
        w_ans = 0 #white로 시작하는 경우
        b_start = 'B'
        for x in board[i:i+8]:
            for y in range(8):
                #black으로 시작한 경우, y가 짝수일 때 !b_start이면 => b_ans+1
                #white로 시작한 경우, y가 짝수일 때 ==b_start이면 => w_ans+1
                if y%2==0:
                    if x[j+y]!=b_start:
                        b_ans+=1
                    else:
                        w_ans+=1
                else:
                    if x[j+y]==b_start:
                        b_ans+=1
                    else:
                        w_ans+=1
            if b_start == 'B':
                b_start = 'W'
            else:
                b_start = 'B'
        ans = min([b_ans, w_ans, ans])
print(ans)
