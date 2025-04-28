from sys import stdin

N, C, W = map(int, stdin.readline().split()) #나무 수, 자르는 비용, 한 단위 가격

woods = [int(stdin.readline()) for _ in range(N)]

# 자른 나무의 길이가 L
# 나무의 개수 K => wood//L
# 나무를 자르는 횟수 M => wood//L (wood%L==0 인 경우 -1)
# 총 가격: KxLxW - CxM

def total_price(l): #모든 나무를 길이 l로 잘라서 팔 때 총 가격
    money = 0
    
    for w in woods:
        k=w//l
        m=w//l
        if w%l==0:
            m-=1
        price = k*l*W-C*m
        if price > 0:
            money+=price
    return money

def max_total_price():
    max_price = 0
    for l in range(1, max(woods)+1):
        curr_price = total_price(l)
        max_price = max(curr_price, max_price)
    return max_price

print(max_total_price())
    
    