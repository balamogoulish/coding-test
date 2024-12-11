def solution(array, commands):
    answer = []
    
    for c in commands:
        i,j,k = c
        #1. i부터 j까지 자름
        arr = array[i-1:j]
        #2. 정렬함
        arr.sort()
        #3. k번째 수를 answer에 담음
        answer.append(arr[k-1])
    
    return answer