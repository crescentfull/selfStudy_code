# bool 변수 알아보기
# bool 변수의 용도는 플래그 변수 형태로 사용을 많이 한다.
# 타 프로그래밍 언어에서는 bool변수의 값은 소문자로 시작하지만 파이썬은 대문자로 시작한다
flag = True
print(type(flag))
print(flag)

flag = not flag
print(type(flag))
print(flag)

if flag:
    print("실행됩니다")
else:
    print("거짓이라서 실행이 안됩니다")