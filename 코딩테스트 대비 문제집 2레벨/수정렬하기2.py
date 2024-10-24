# 단순 수 정렬이지만, 시간 복잡도를 따지는 문제
# input() 대신 stdin.readline()을 사용하면 입력에 대한 시간을 줄일 수 있다

# https://www.acmicpc.net/problem/2751
from sys import stdin
n = int(stdin.readline())
arr=[]
for _ in range(n):
    arr.append(int(stdin.readline()))
arr = sorted(arr)
for a in arr:
    print(a)
