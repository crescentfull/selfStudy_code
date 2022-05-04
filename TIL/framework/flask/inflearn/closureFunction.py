def outer_func(num):
    # 중첩 함수에서 외부 함수의 변수에 접근 가능
    def inner_func():
        print(num)
        return '안녕'
    
    return inner_func                 # 중첩 함수 이름을 리턴합니다.

closure_func = outer_func(10)    # <--- First-class function
closure_func()            # <--- Closure 호출 

def calc_power(n):
    def power(digit):
        return digit ** n
    return power

power2 = calc_power(2)
power3 = calc_power(3)
power4 = calc_power(4)

print (power2(2))
print (power3(2))
print (power4(2))
print(calc_power)
list_data = list()
for num in range(1,6):
    list_data.append(calc_power(num)) #list_data에 원소 각각이 클로져함수가 된다
print(list_data[0])
    
for func in list_data:
    print(func(2))