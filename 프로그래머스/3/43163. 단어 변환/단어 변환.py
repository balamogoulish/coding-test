'''
최단 경로 문제
1. curr에서 words의 문자들 중, 갈 수 있는 경우 nxts를 구한다. => 한 단어만 바껴야 하고, 방문하지 않은 단어
2. nxt로 가서 반복
3. 만약 target과 같아지면 이 횟수를 return
'''


def available(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i]!=word2[i]:
            cnt+=1
    if cnt==1:
        return 1
    if cnt==0:
        return -1
    return 2


def solution(begin, target, words):
    answer = [51]
    
    visited = [False for _ in range(len(words))]
    
    def dfs(curr, cnt):
        for nxt in range(len(words)):
            if available(words[nxt], curr) == 1 and not visited[nxt]:
                if available(words[nxt], target) == -1:
                    answer[0] = min(answer[0], cnt)
                else:
                    visited[nxt] = True
                    dfs(words[nxt], cnt+1)
                    
    if target not in words:
        return 0
    dfs(begin, 1)
    
    
    
    return answer[0]