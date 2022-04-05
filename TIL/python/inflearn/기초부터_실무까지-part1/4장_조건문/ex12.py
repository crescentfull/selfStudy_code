# 논리연산자(logical operator)는 두 개 이상의 조건을 조합해서 참인지 거짓인지 판별
# and(논리곱), or(논리합), not(논리부정)
# not은 논리값을 뒤집어 버리는 것 참 => 거짓, 거짓 => 참
# and 논리 연산자의 실습
name = "가나다"
age = 14
height = 160

# and 논리연산자는 여러 조건중에서 처음 조건이 거짓이라면 다른조건은 검사하지 않고 종료.(단축계산)
if(age>=14) and (height>=160) and (name == "가나다"):
    print(name+"님은 놀이기구를 탈 수 있습니다.")
else:
    print(name+"님은 놀이기구를 탈 수 없습니다.")
print("---------------------------------------")
# or 논리연산자는 여러 조건중에서 처음 조건이 거짓이라면 다른조건은 검사하지 않고 종료.(단축계산)
if(age>=15) and (height>=160) and (name == "가나다"):
    print(name+"님은 놀이기구를 탈 수 있습니다.")
else:
    print(name+"님은 놀이기구를 탈 수 없습니다.")
print("---------------------------------------")
#not 실습
#논리부정연산자인 not은 조건이 참이면 전체 조건식의 결과를 반대(거짓)로 만듬. 반대의 경우도 마찬가지
if not(1 == 1):
    print("참입니다.")
else:
    print("거짓입니다")