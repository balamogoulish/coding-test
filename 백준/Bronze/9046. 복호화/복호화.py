from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    secret = stdin.readline().split('\n')[0]
    num_s = [0]*26
    max1_s = 0
    max2_s = 0
    for s in secret:
        if s==' ':
            continue
        curr = ord(s)-97
        num_s[curr]+=1
        if num_s[curr] >= num_s[max1_s]:
            max2_s = max1_s
            max1_s = curr

    if num_s[max1_s] == num_s[max2_s] and max1_s!=max2_s:
        print("?")
    else:
        print(chr(max1_s+97))