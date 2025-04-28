from sys import stdin

n = int(stdin.readline())
words = [stdin.readline().strip() for _ in range(n)]
answer = 0

def checkSimilar(wordA, wordB):
    # dict로 key:wordA의 알파벳, value:wordB의 알파벳
    # dict에 a가 없으면 a:b로 등록
    # dict에 a가 있는데 value가 다르면 False 반환
    
    a = dict()
    b = dict()
    
    for i in range(len(wordA)):
        if wordA[i] in a:
            if a[wordA[i]] != wordB[i]:
                return False
        else:
            if wordB[i] in b:
                if b[wordB[i]] != wordA[i]:
                    return False
            b[wordB[i]] = wordA[i]
            a[wordA[i]] = wordB[i]
    return True
    
for i in range(n):
    for j in range(i+1, n):
        if checkSimilar(words[i], words[j]):
            answer+=1
print(answer)