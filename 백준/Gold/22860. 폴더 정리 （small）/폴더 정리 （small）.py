from sys import stdin,setrecursionlimit
setrecursionlimit(2000)  # 재귀 깊이 제한 증가

n, m = map(int, stdin.readline().split()) #n: 폴더 개수, m: 파일 개수
folders = {"main":[[], []]} #폴더명:[[하위 폴더 배열],[파일 배열]]
for _ in range(n+m):
    upper, now, isFolder = stdin.readline().strip().split();
    if upper not in folders:
        folders[upper] = [[],[]]
    if isFolder=='1':
        folders[upper][0].append(now)
        if now not in folders:
            folders[now]=[[],[]]
    else:
        folders[upper][1].append(now)

def getFiles(curr):
    nxtFiles = []
    for nxt in folders[curr][0]:
        nxtFiles+=getFiles(nxt)
    folders[curr][1]+=nxtFiles
    return folders[curr][1]

getFiles('main')

q = int(stdin.readline())

for _ in range(q):
    curr = stdin.readline().strip().split('/')[-1]
    files = folders[curr][1]
    cnt = len(files)
    type_cnt = len(set(files))
    print(type_cnt, cnt)
    