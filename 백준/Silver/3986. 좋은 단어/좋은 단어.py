from sys import stdin

n = int(stdin.readline())
answer = 0

for _ in range(n):
    word = stdin.readline().strip()
    st = []
    for w in word:
        if len(st)==0:
            st.append(w)
            continue
        prev = st.pop()
        if prev != w:
            st.append(prev)
            st.append(w)
    if len(st)==0:
        answer+=1
print(answer)
        