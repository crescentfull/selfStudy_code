# 디폴트 인수(default argument)
# 함수의 매개변수가 기본 값을 가지게 한다.

def defaultFunc(name, msg='hello'):
    print(name,msg)
    return

# 함수의 인수가 2개이지만 디폴트 인수가 존재함으로 함수의 매개변수가 1개만 있어도 함수가 실행됨
defaultFunc('송영록')

# 2번째 인수에 다른 매개변수를 넣으면 디폴트값이 아닌 주어진 매개변수로 대체된다.
defaultFunc('송영록','반가워')