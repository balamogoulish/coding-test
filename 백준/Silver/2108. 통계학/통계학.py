#https://www.acmicpc.net/problem/1181
from collections import Counter
from sys import stdin
n = int(stdin.readline())
arr = []

for _ in range(n):
    arr.append(int(stdin.readline()))
arr = sorted(arr)
counter = Counter(arr)
counter = sorted(counter.items(), key=lambda x:-x[1] )

print(int((round(sum(arr)/n, 0))))
print(arr[n//2])
if len(counter)>1 and counter[0][1]==counter[1][1]:
    print(counter[1][0])
else:
    print(counter[0][0])
print(int(arr[-1])-int(arr[0]))