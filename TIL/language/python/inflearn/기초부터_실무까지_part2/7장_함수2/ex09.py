# 매개변수는 함수의 선언부에 존재하며 함수가 호출될 때 비로소 메모리에 할당이 된다.
# 함수가 종료되면 매개변수도 소멸이 된다.
# 매개변수가 지역변수의 일종이다.

def test_list(my_list):
    my_list = [1,2,3,4] # 매개변수로 넘어온 my_list에 새로운 리스트를 할당한다.
    print("함수 안에서 my_list 값 출력 : ", my_list)
    return

my_list = [100,200,300,400]
test_list(my_list)
print('함수 실행 후 my_list 값 : ', my_list)