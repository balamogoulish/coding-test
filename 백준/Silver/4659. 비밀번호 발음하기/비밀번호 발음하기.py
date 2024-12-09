from sys import stdin

#높은 품질인 경우
#1. a, e, i, o, u 중 적어도 하나를 포함
#2. 모음 or 자음이 3개 연속 불가
#3. 'ee', 'oo'를 제외한 같은 글자 연속 불가가

vowel = ['a', 'e', 'i', 'o', 'u']

def printNotAcc (s):
    print('<'+s+'> is not acceptable.')

while True:
    pw = stdin.readline().split('\n')[0]
    
    if pw=='end': #end인 경우 끝
        break
    
    #1. 모음을 적어도 하나 포함
    if not any(str in pw for str in vowel):
        printNotAcc(pw)
        continue
    
    #2,3. 모음 or 자음이 3개 연속 불가, 같은 글자 연속 불가
    p0 = pw[0]
    isAcc=True
    if len(pw)>1:
        p1 = pw[1]
        if p0==p1 and p0 not in ['e', 'o']:
            printNotAcc(pw)
            continue
    for i in range(2, len(pw)):
        p2 = pw[i]
        if (p0 in vowel and p1 in vowel and p2 in vowel) or (p0 not in vowel and p1 not in vowel and p2 not in vowel):
            isAcc=False
            break
        if p1 == p2 and p1 not in ['e', 'o']:
            isAcc=False
            break
        p0=p1
        p1=p2
    if isAcc:
        print('<'+pw+'> is acceptable.')
    else:
        printNotAcc(pw)
    

