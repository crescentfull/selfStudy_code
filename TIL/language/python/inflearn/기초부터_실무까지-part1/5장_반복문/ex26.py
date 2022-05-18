statement = "             hi"
# 왼쪽 공백만 제거하는 함수 (lstrip)
print("원본 : ", statement)
print("함수 적용 : ", statement.lstrip())
print("*******************")
#오른쪽 공백제거하는 함수(rstrip)
statement = "    hi               "
print("원본 : ", statement)
print("함수 적용 : ", statement.rstrip())
print("*******************")
#양쪽(strip)
statement = "            hi               "
print("원본 : ", statement)
print("함수 적용 : ", statement.strip())
print("*******************")

#문자열 나누기
print("*******************")
statements = "나는 문자를 나누려 합니다"
print(statements.split())