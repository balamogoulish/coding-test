from sys import stdin

trees = {}
cnt = 0
while True:
    tree = stdin.readline().strip()
    if tree == '':
        break
    if tree not in trees:
        trees[tree] = 0
    trees[tree]+=1
    cnt+=1

trees = sorted(trees.items(), key=lambda x:x[0])
for t in trees:
    print("%s %.4f" %(t[0], t[1]/cnt*100))