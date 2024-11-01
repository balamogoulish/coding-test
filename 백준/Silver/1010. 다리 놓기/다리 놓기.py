from sys import stdin
from itertools import combinations

x = int(stdin.readline())

for _ in range(x):
    n , m = map(int, stdin.readline().split())
    #다리는 겹쳐질 수 없기 때문에 무조건 순서는 정해져 있다고 볼 수 있음음
    # mCn = mPn/n!
    mPn = 1
    n_fac = 1
    for i in range(1, n+1):
        n_fac *= i
        mPn *= m
        m-=1
    print(int(mPn/n_fac))