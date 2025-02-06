def solution(n, times):
	# 가능한 최솟값과 최댓값을 left와 right로 설정
    left = 1
    right = max(times) * n
    
    # 이분탐색이니 left가 right 이하인 동안
    while left <= right:
        mid = (left+right)//2
        people = 0 # 심사한 사람 수
     	
        for time in times:
        	# 해당 심사대에서 주어진 시간동안 심사 받은 수 더하기
            people += mid//time
            if people >= n:
                break
        
        # n명 이상 심사했다면, 시간이 남을 가능성 O
        if people >= n:
            answer = mid
            right = mid -1
        # n명 미만 심사했다면, 시간이 너무 부족하다
        else :
            left = mid + 1
    return answer