'''
n: 지방 수 (3~10,000)
pays: 예산들 (각각 1~100,000)
m: 총 예산 (n~1,000,000,000)

-> 예산의 최대 상한값은?
'''

from sys import stdin

n = int(stdin.readline())
pays = list(map(int, stdin.readline().split()))
m = int(stdin.readline())

min_pay = 1
max_pay = max(pays)

#상한선이 x일때, 소모 예산 
def total_pays(x):
    totals = 0
    for pay in pays:
        if pay > x: #예산 요청이 상한선 이상인 경우
            totals+=x
        else:
            totals+=pay
    return totals

#최대 상한값 찾기
def max_avail_pay(min_pay, max_pay):
    answer = 0
    while True:
        mid = (min_pay+max_pay)//2
        mid_total = total_pays(mid)
        
        if mid_total > m: #총예산보다 소모예산이 크면 예산을 줄여야 함
            max_pay = mid-1
        else: #총예산보다 소모예산이 작거나 같으면 예산을 키워도 됨
            answer = max(answer, mid)
            min_pay = mid+1
        
        if min_pay > max_pay:
            return answer

print(max_avail_pay(min_pay, max_pay))

    
    