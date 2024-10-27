from sys import stdin

k = int(stdin.readline())
ans = []
for _ in range(k):
    x = int(stdin.readline())
    if x==0:
        ans.pop()
    else:
        ans.append(x)
print(sum(ans))