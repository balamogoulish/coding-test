def solution(operations):
    answer = []
    dq = []
    for operation in operations:
        op, num = operation.strip().split()
        if op=='I':
            dq.append(int(num))
            dq.sort()
        else:
            if num=='-1' and dq:
                dq.pop(0)
            elif num=='1' and dq:
                dq.pop()
    if dq:
        answer = [max(dq), min(dq)]
    else:
        answer = [0, 0]
    
    return answer