from sys import stdin

a, b = map(int, stdin.readline().split())

def a_to_b(curr, cnt):
    if curr==b:
        print(cnt)
        exit()
    if curr<b:
        a_to_b(curr*2, cnt+1)
        a_to_b(int(str(curr)+'1'), cnt+1)
a_to_b(a, 1)
print(-1)