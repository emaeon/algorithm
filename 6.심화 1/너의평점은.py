import sys

input = sys.stdin.readline

#전공평점 >= 3.3 
#전공 평점 : 과목 당 (학점 * 과목평점) / 총 학점
#20줄

score_lst=[4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
grade_lst=['A+','A0','B+','B0','C+','C0','D+','D0','F']


cnt = 0
score=0
for _ in range(20):
    subject, number, grade = map(str,input().split())
    if grade in grade_lst :
        score += float(number) * score_lst[grade_lst.index(grade)]
        cnt += float(number)
    else:
        pass

print(score/cnt)
        

    



