from sys import stdin

T = int(stdin.readline().split('\n')[0])

for _ in range(T):
    W = stdin.readline().split('\n')[0]
    K = int(stdin.readline().split('\n')[0])
    cnt = [[] for i in range(26)]
    min_k = 100000
    max_k = -1
    for i in range(len(W)):
        cnt[ord(W[i])-97].append(i)
    for i in range(26):
        if len(cnt[i])>=K:
            for j in range(K-1, len(cnt[i])):
                x = cnt[i][j-K+1:j+1]
                min_k = min(min_k, x[-1]-x[0]+1)
                max_k = max(max_k, x[-1]-x[0]+1)
    if min_k==100000 and max_k==-1:
        print(-1)
    else:
        print(min_k, max_k)