from collections import deque

def solution(n, wires):
    answer = n
    tree = [[] for _ in range(n+1)]
    visited = []
    for w in wires:
        tree[w[0]].append(w[1])
        tree[w[1]].append(w[0])
        
    def getNumOfNode(x, v1, v2):
        q = deque([x])
        visited[x] = True
        cnt = 0
        while q:
            curr = q.popleft()
            cnt+=1
            for nxt in tree[curr]:
                if not visited[nxt]:
                    if nxt not in [v1, v2]:
                        q.append(nxt)
                        visited[nxt] = True
        return cnt
    
    for v1 in range(1, n+1):
        for v2 in range(v1+1, n+1):
            if v2 in tree[v1]: #v1과 v2가 연결되어 있다면, 연결을 끊고 각 영역의 송전탑 개수의 차이를 구함
                visited = [False for _ in range(n+1)]
                cnt1 = getNumOfNode(v1, v1, v2)
                visited = [False for _ in range(n+1)]
                cnt2 = getNumOfNode(v2, v1, v2)
                answer = min(answer, abs(cnt1-cnt2))
    return answer