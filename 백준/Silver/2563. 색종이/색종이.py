answer=[]

N = int(input())
for _ in range(N):
    x, y = input().split()
    x, y =int(x), int(y)
    for i in range(x, x+10):
        for j in range(y, y+10):
            if (i, j) in answer:
                continue
            else:
                answer.append((i, j))
print(len(answer))