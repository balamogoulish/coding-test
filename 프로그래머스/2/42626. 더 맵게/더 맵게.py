import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        h0 = heapq.heappop(scoville)
        if h0 >= K:
            break
        if len(scoville)<1:
            return -1
        h1 = heapq.heappop(scoville)
        heapq.heappush(scoville, h0+(h1*2))

        answer+=1
    return answer