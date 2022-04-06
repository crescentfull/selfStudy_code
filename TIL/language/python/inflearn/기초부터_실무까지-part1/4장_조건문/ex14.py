# 몸무게와 키를 입력받고 BMI가 20.0이상이고 25미만이면 "표준" 출력
# 아니라면 체중관리가 필요하다고 출력
# BMI = 몸무게 / (키*키)

height = float(input("키(cm)를 입력하시오 : "))
weight = float(input("몸무게(kg)를 입력하시오 : "))
height /= 100.0 #복합대입연산자155
BMI = weight / (height*height) #height**2 도 가능, 하지만 가독성때문에

print("BMI", round(BMI,2))
