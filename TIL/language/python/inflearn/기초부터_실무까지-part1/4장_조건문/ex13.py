# 대학교를 졸업하려면 적어도 140학점을 이수해야 하고 평점은 2.0은 되어야 한다고 해보자
# 이것을 프로그램으로 만들어 보자
#사용자에게 이수학점과 평점을 입력받아서 졸업가능 여부를 확인하는 코드를 작성해보라
classtime = float(input("학점을 입력하시오 : "))
avr_grade = float(input("평점을 입력하시오 : "))

if (classtime >= 140) and (avr_grade>=2.0):
    print("success")
else:
    print("nope")
    
