def solution(brown, yellow):
    answer = []
    for i in range(1, int(yellow**(0.5)+1)):
        if yellow%i==0:
            yellow_w = i
            yellow_h = yellow//i
            if (brown+yellow)==(yellow_h+2)*(yellow_w+2):
                return [yellow_h+2, yellow_w+2]
    return answer