# 세 정수의 최댓값 구하기

print('세 정수의 최댓값을 구한다')
a = int(input("정수 a의 값 : "))
b = int(input("정수 b의 값 : "))
c = int(input("정수 c의 값 : "))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c

print(f"최댓값은 {maximum}입니다.")

# 이렇게 한문장씩 순서대로 처리되는 구조를 순차구조 sequential structure라고 한다.
# 조건식으로 평가한 결과에 따라 프로그램의 실행 흐름이 변경되는데 이러한 구조를 선택구조 select structure라고 한다.