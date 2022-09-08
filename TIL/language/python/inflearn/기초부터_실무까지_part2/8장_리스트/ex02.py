# 학생 성적 처리하는 프로그램 만들기
# 조건 : 사용자로부터 성적을 입력을 받아서 리스트에 저장
# 성적의 평균을 구하고 해당 점수가 80점 이상 성적을 받은 학생의 수를 출력
# 출력 결과 예시
# 성적을 입력하시오 : 10
# 성적을 입력하시오 : 20
# 성적을 입력하시오 : 30
# 성적평균은 {}입니다.

student = int(input("학생 수 입력 : "))
student_score = []
score_sum = 0
cnt = 0
for i in range(student):
    if i > student:
        break
    else:
        score = int(input("성적을 입력하시오 : "))
        student_score.append(score)
        score_sum += student_score[i]
        if score >= 80:
            cnt += 1
print("학생 점수 리스트 : ",student_score)
print("총 점수 : ", score_sum)
print("점수 평균 : ",score_sum/student)
print("80점이상 학생 수 : ",cnt)