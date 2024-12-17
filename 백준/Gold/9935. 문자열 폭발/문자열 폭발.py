from sys import stdin

tmp = stdin.readline().strip()
bomb = stdin.readline().strip()
ans = []
# 시간 초과
# while True:
#     tmp = tmp.split(bomb)
#     tmp = "".join(tmp)
#     if bomb not in tmp:
#         break
# if tmp=='':
#     print("FRULA")
# else:
#     print(tmp)
    
for t in tmp:
    ans.append(t)
    while True:
        if bomb != "".join(ans[-len(bomb):]):
            break
        else:
            for i in range(len(bomb)):
                ans.pop()
x= "".join(ans)
if x=="":
    print("FRULA")
else:
    print(x)