from collections import deque

def solution(n, w, num):
    answer = 0
    h = n//w
    if n%w>0:
        h+=1
    boxes= []
    
    i=1
    tmp = []
    while i<=n:
        tmp.append(i)
        if i%w==0:
            if (i//w)%2==1:
                tmp.sort()
                # print('right', tmp)
            else:
                tmp.sort(reverse=True)
                # print('reverse', tmp)
            boxes.append(tmp)
            # print(boxes)
            tmp = []
        i+=1
    
    if len(tmp) > 0:
        if (tmp[0]//w)%2==0:
            tmp.sort()
            last = deque(tmp)
            for x in range(w-len(tmp)):
                last.append(0)
            # print('right', last)
        else:
            tmp.sort(reverse=True)
            last = deque(tmp)
            for x in range(w-len(tmp)):
                last.appendleft(0)
            # print('reverse', last)
        boxes.append(list(last))
    
    # print(h, w)
    for y in range(h):
        for x in range(w):
            if boxes[y][x]==num:
                answer = h-y
                if boxes[h-1][x]!=0:
                    answer+=1
                return answer-1
    
    return answer