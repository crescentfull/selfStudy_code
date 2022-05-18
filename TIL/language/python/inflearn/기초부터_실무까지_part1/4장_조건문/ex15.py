# if ~ elif ~ else(옵션) 실습

score = int(input("성적을 입력하세요(0~100) : "))
#다중조건중 하나만 만족하면 그 이후의 조건은 검사하지 않는다.
if score >= 90:
    print("학점 A")
elif score >= 80:
    print("학점 B")
elif score >= 70:
    print("학점 C")
else:#else 구문은 옵션이지만 다중 조건을 설정할때는 조건을 명시할수 없다.
    print("학점 F")