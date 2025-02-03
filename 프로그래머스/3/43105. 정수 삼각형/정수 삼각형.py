def solution(triangle):
    
    for i in range(len(triangle)-1, 0, -1):
        tmp = [[] for _ in range(i)]
        for j in range(i+1):
            if j-1>=0: #왼쪽 부모
                tmp[j-1].append(triangle[i-1][j-1]+triangle[i][j])
            if j<i: #오른쪽 부모
                tmp[j].append(triangle[i-1][j]+triangle[i][j])
        for k in range(len(tmp)):
            triangle[i-1][k] = max(tmp[k])
    return triangle[0][0]