from sys import stdin

n = int(stdin.readline())
col = [0 for _ in range(1001)]
max_y = 0
answer = 0
max_f_x = 0
max_b_x = 0

b_prev = 0

for _ in range(n):
    cx, cy = map(int, stdin.readline().split())
    col[cx] =cy
    if max_y < cy:
        max_y = cy

f_prev = 0
for i in range(1001):
    if col[i]>f_prev:
        f_prev = col[i]
    if f_prev == max_y:
        max_f_x = i
        break
    answer+=f_prev
    
for i in range(1001):
    if col[1000-i]>b_prev:
        b_prev = col[1000-i]
    
    if b_prev == max_y:
        max_b_x = 1000-i
        break
    answer+=b_prev
    
print(answer+(max_b_x-max_f_x+1)*max_y)