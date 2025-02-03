def solution(N, number):
    answer = -1
    dp = [[] for _ in range(9)]
    nums = set([])
    
    if N==number:
        return 1
    
    # 사칙연산을 수행하는 함수
    def cal(a, b):
        tmp = []
        tmp.append(a + b)
        tmp.append(a - b)
        tmp.append(a * b)
        tmp.append(b - a)
        if a != 0:
            tmp.append(b // a)
        if b != 0:
            tmp.append(a // b)
        return tmp
    
    # 첫 번째 dp[1]을 초기화: N을 한 번만 사용하는 경우
    tmp = 0
    for i in range(1, 9):
        tmp = tmp * 10 + N
        if tmp==number:
            return i
        dp[i].append(tmp)
        # 이전의 dp[i]와 dp[j]를 이용해 새로운 숫자를 만들기
        for j in range(1, i+1):
            if i+j>8:
                return -1
            for a in dp[i]:
                for b in dp[j]:
                    result = cal(a, b)  # 연산 결과를 구하기
                    for r in result:
                        if r not in nums:
                            nums.add(r)
                            dp[i+j].append(r)
                    
                    # 목표 숫자 찾으면 즉시 반환
                    if number in dp[i + j]:
                        return i + j
    
    return answer
