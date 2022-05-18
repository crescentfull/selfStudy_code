# 두 개의 정수를 입력받아서 두 수 중에서 더 큰 수를 리턴하는 함수를 작성

# def bigger(first,second):
#     print(f"{first}와 {second}를 입력하였습니다.")
#     if first < second:
#         return print(f"{second}(이)가 더 큰 숫자 입니다.")
#     else:
#         return print(f"{first}(이)가 더 큰 숫자 입니다.")
# !return 갯수는 최소화 하여 주는게 좋은 코드이다.
def bigger(first,second):
    print(f"{first}와 {second}를 입력하였습니다.")
    res = 0
    if first < second:
        res = second
    else:
        res = first
    return print("더 큰 값 : ", res)