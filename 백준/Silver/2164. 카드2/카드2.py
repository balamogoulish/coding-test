from sys import stdin
from collections import deque

n = int(stdin.readline())
cards = deque([i for i in range(1, n+1)])

isAppend=False #버림
while len(cards)!=1:
    x = cards.popleft()
    if isAppend:
        cards.append(x)
        isAppend= False
    else:
        isAppend=True

print(cards[0])