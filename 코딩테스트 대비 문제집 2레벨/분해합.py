#https://www.acmicpc.net/problem/2231

## 답이 틀린 것은 아니지만 런타임에러 발생...
## 시간을 더 줄일 수 있는 방법이 있나?
n = int(input())
ans = 0

for i in range(n-9*len(str(n)), n):
    if (i +sum(list(map(int, str(i))))) == n:
        ans = i
        break
print(ans)

## 다음과 같이 min을 설정해야 한다.
## n-9*len(str(n))이 음수가 되는 경우도 있기 때문인 것 같음!!
n = int(input())

min = n-9*len(str(n))
if min<1:
    min=1
for i in range(min, n+1):
    if (i +sum(list(map(int, str(i))))) == n:
        print(i)
        break
    if i==n:
        print(0)
