#https://www.acmicpc.net/problem/1018

n, m = map(int, input().split())
board = []
ans = 64

for _ in range(n):
    temp = input()
    s = []
    for t in temp:
        s.append(t)
    board.append(s)

for i in range(n-7):
    for j in range(m-7):
        for x in board[i:i+8]:
            print(x[j:j+8])
        print()
