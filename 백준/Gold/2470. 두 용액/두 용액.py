from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()

left = 0
right = N-1

answer = [arr[0], arr[1]]
min_sum = arr[0]+arr[1]

while left<right:
    tmp = arr[left]+arr[right]
    if abs(min_sum) > abs(tmp):
        min_sum = tmp
        answer[0], answer[1] = arr[left], arr[right]
        
    if tmp==0:
        print(arr[left], arr[right])
        exit()
    elif tmp>0:
        right-=1
    else:
        left+=1
        
print(answer[0], answer[1])