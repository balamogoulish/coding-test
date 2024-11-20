from sys import stdin

n = int(stdin.readline())
arr = []

for _ in range(n):
    arr.append(int(stdin.readline()))
arr.sort(reverse=True)

tip = 0
for i in range(n):
    if arr[i]-i<0:
        break
    else:
        tip+=arr[i]-i
print(tip)