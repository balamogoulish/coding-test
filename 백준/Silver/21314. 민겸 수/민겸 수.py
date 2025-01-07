from sys import stdin

#가장 큰 수 => M...MK 구조로 끊는다.
#가장 작은 수 => M...M, K 구조로 끊는다.

MK = [a for a in stdin.readline().strip()]

m_cnt, k_cnt = 0, 0
answer = ''

#최댓값
for mk in MK:
    if mk=='M': #m인 경우
        if m_cnt==0: #이전에 m이 아닌 경우 5를 k의 개수만큼 더함
            answer+='5'*k_cnt
            k_cnt=0
        m_cnt+=1
            
    else: #k인 경우
        if k_cnt==0 and m_cnt>0: #m...mk인 경우 10^(m_cnt-1)만큼 더함
            answer+=str(10**(m_cnt)*5)
            m_cnt=0
        else:
            k_cnt+=1
if m_cnt>0:
    print(answer+'1'*m_cnt)
else:
    print(answer+'5'*k_cnt)
    
m_cnt, k_cnt = 0, 0
answer = ''
#최솟값
for mk in MK:
    if mk=='M': #m인 경우
        if m_cnt==0: #이전에 m이 아닌 경우 5를 k의 개수만큼 더함
            answer+='5'*k_cnt
            k_cnt=0
        m_cnt+=1
            
    else: #k인 경우
        if k_cnt==0 and m_cnt>0: #m...mk인 경우 10^(m_cnt-1)만큼 더함
            answer+=str(10**(m_cnt-1))
            m_cnt=0
        k_cnt+=1

if m_cnt>0:
    print(answer+str(10**(m_cnt-1)))
else:
    print(answer+'5'*k_cnt)
            