def solution(n, lost, reserve):
    a = n-len(lost)
    b = n-len(lost)
    lost.sort()
    reserve.sort()
    lost_c = list()
    
    for l in lost: #reserve와 lost가 같은 것 우선 제외
        if l in reserve:
            reserve.pop(reserve.index(l))
            a+=1
            b+=1
        else:
            lost_c.append(l)
    
    for l in lost_c:
        if l-1 in reserve:
            reserve.pop(reserve.index(l-1))
            a+=1
        elif l+1 in reserve:
            reserve.pop(reserve.index(l+1))
            a+=1
            
    reserve_copy = [r for r in reserve]
    for l in lost_c:
        if l+1 in reserve_copy:
            reserve_copy.pop(reserve_copy.index(l+1))
            b+=1
        elif l-1 in reserve_copy:
            reserve_copy.pop(reserve_copy.index(l-1))
            b+=1

    if a>b: 
        return a
    else: 
        return b
            
            