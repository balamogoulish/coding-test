from sys import stdin

n = int(stdin.readline())
words = []
answer = ['', '', n+1, n+1] # S, T, indexOfS, indexOfT
cnt = 0

tmp = set([])

for i in range(n):
    w = stdin.readline().strip()
    if w not in tmp:
        words.append((w, i))
        tmp.add(w)

for i in range(len(words)):
    for j in range(i+1, len(words)):
        same = 0
        x= min(len(words[i][0]), len(words[j][0]))
        for k in range(x):
            if words[i][0][k]!=words[j][0][k]:
                break
            same+=1
        if same>cnt:
            answer[0]=words[i][0]
            answer[1]=words[j][0]
            answer[2]=words[i][1]
            answer[3]=words[j][1]
            cnt=same
        elif same==cnt:
            if answer[2]>words[i][1]:
                answer[0]=words[i][0]
                answer[1]=words[j][0]
                answer[2]=words[i][1]
                answer[3]=words[j][1]
                cnt=same
            elif answer[2]==words[i][1] and answer[3]>words[j][1]:
                answer[0]=words[i][0]
                answer[1]=words[j][0]
                answer[2]=words[i][1]
                answer[3]=words[j][1]
                cnt=same
print(answer[0])
print(answer[1])