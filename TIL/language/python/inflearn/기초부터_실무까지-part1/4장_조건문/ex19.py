# 사용자로부터 태어난 연도를 입력받아서 초등학생, 중학생, 고등학생, 대학생 중에서 어디에 해당하는지 출력
# 이외의 나이라면 일반인
from datetime import *

bornIn = int(input("태어난 년도를 입력하시오 : "))

age = datetime.today().year - bornIn
print(age)

if (13>= age >=8):
    print("초등학생")
elif (16>= age >= 14):
    print("중학생")
elif (19>= age >= 17):
    print("고등학생")
elif (27>= age >= 20):
    print("대학생")
elif (8>age):
    print("유아")
else:
    print("일반인")