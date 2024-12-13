from sys import stdin

S = stdin.readline().split('\n')[0]
answer=''
tag=''#tag가 끝나면 비움, tag는 뒤집지 않음
word='' #단어

for s in S:
    if tag=='': #tag내부가 아닌 경우 => 뒤집을 수 있는 단어
        if s=='<': #'<'인 경우 tag 시작 => word를 뒤집어서 answer에 더함
            tag+=s
            answer+=word
            word=''
        elif s==' ':  #공백인 경우
            answer+=word+' '
            word=''
        else: #공백도 아닌 경우
            word=s+word
    
    else: #tag 내부인 경우 => '>'가 아니면 tag에 넣음
        tag+=s
        if s=='>': #tag가 닫힘
            answer+=tag
            tag=''
print(answer+word)