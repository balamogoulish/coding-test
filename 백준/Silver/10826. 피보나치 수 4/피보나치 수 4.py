from sys import stdin

n = int(stdin.readline())
if n==0:
    print(0)
else:
    f0 = 0
    f1 = 1
    f2 = 1
    for i in range(n-1):
        f2 = f0+f1
        f0 = f1
        f1 = f2
    print(f2)