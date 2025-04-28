from sys import stdin

n = int(stdin.readline())
alphabets = []

for i in range(n):
    original = stdin.readline().strip()
    options = list(map(str, original.split(' ')))
    
    result = ""
    isSuccess = False
    
    # 1. 첫 번째 글자가 최초인 경우
    for option in options:
        # isSuccess라면, 이미 단축키를 찾음 -> 그냥 이어붙이면됨
        if isSuccess:
            result+=option+" "
        
        elif option[0].lower() not in alphabets:
            # alpabets에 추가하고, isSuccess를 true로 만듦
            alphabets.append(option[0].lower())
            isSuccess = True
            result +="["+option[0]+"]"+option[1:]+" "
        
        else:
            result +=option+" "
             
    
    # isSuccess라면, 이미 1번에서 단축키 찾기를 성공함 -> 2번은 수행할 필요 X
    # 2. 다른 글자가 최초인 경우
    if isSuccess:
        print(result)
        continue
    result = ""
    for option in options:
        if isSuccess:
            result+=option+" "
            continue
        for s in option:
            if s.lower() not in alphabets and not isSuccess:
                result+="["+s+"]"
                alphabets.append(s.lower())
                isSuccess = True
            else:
                result+=s
        result+=" "
        
    
    # 3. 여기까지 왔다는 건, 단축키가 없다는 것 -> original을 그대로 출력 
    if isSuccess:
        print(result)
        continue
    print(original)
    