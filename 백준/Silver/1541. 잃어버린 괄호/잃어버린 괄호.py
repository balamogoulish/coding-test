from sys import stdin

# 55-50+40 => -뒤를 최대로 만들어야 함
# 1. -를 기준으로 끊음 (55, 50+40)
# 2. +를 기준으로 끊음 (55, (50, 40))
# 3. 각 배열의 합을 구함 (55, 90)
# 4. 배열을 돌면서 뺌
arr = stdin.readline().split('-')
arr_int = []
for i in range(len(arr)):
    arr_int.append(list(map(int,arr[i].split('+'))))
answer = sum(arr_int[0])
for i in range(1,len(arr_int)):
    tmp=(sum(arr_int[i]))
    answer-=(tmp)
print(answer)