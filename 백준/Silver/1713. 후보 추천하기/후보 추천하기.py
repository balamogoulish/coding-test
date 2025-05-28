from sys import stdin

def solution():
    n = int(stdin.readline()) #사진틀 수
    m = int(stdin.readline()) #추천 수
    recommends = list(map(int, stdin.readline().split())) #추천 목록
    students = {} #students[i]=[j, k] => i번 학생의 추천 수 j, 추천받은 시간 k(k가 작을 수록 오래 전에 추천 받음)
    pictures = [] #사진틀에 들어있는 학생 수
    
    for t in range(m):
        #t: 추천받은 시간
        #r: 추천받은 학생
        r = recommends[t]
        
        if r not in pictures: #추천받은 학생이 사진틀에 없는 경우
            if len(pictures)<n: #사진틀이 남은 경우
                pictures.append(r)
                
            else: #사진틀이 꽉 찬 경우
                deleted_student_index = 0
                min_recommended_cnt, min_recommended_t = map(int, students[pictures[0]])
                for j in range(1, n):
                    p = pictures[j]
                    if min_recommended_cnt > students[p][0] or (min_recommended_cnt == students[p][0] and min_recommended_t > students[p][1]):
                        min_recommended_cnt = students[p][0]
                        min_recommended_t = students[p][1]
                        deleted_student_index = j
                deleted_student = pictures[deleted_student_index]
                pictures[deleted_student_index] = r
                students[deleted_student] = [0, 0]

                #print('removed: ', deleted_student)
            if r not in students:
                students[r]=[]
            students[r] = [1, t]
        else:
            students[r][0]=students[r][0]+1
        #print(students, pictures)
            
    pictures.sort()
    for p in pictures:
        print(p, end=' ')
        
    
solution() 
                
                
                
                