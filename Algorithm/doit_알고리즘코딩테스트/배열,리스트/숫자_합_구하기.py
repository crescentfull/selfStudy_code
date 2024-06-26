'''
숫자 합 구하기

N개의 숫자가 공백 없이 써 있다. 
이 숫자를 모두 합해 출력하는 프로그램을 작성하시오.

# 입력
1번째 줄에 숫자의 개수 N(1 <= N <= 100), 2번째 줄에 숫자 N개의 공백 없이 주어진다.

#출력

입력1
1 / 1
출력1
1

입력2
5/ 54321
출력2
15

입력3
25 / 70000000000000000000000
출력3
7

'''
'''
수기 풀이
리스트 자료 구조를 이용해서 해결가능
주어진 숫자 리스트 형태로 저장 -> 해당 리스트 index를 탐색 -> 각 자릿수의 값을 더해주자
자릿수를 더할 때는 정수형으로 변환해준다.

 - pseudocode
n값 받기
numbers 변수에 list 함수를 이용하여 숫자를 한 자리씩 나누어 받기.
sum 변수 선언

for numbers 탐색:
    sum 변수에 numbers에 있는 각 자릿수 가져와서 더하기
sum 출력
'''

# 문제 북석
# 리스트 사용, 12


numbers = list((input())) #input으로 들어온 값들을 리스트로 변환
print(numbers) #확인

sum = 0 # sum 변수 초기화

for i in numbers: # for문으로 리스트에 저장된 index 순환 탐색
    sum = sum + int(i) # 리스트 값 출력
    
print(sum)

# 제발 이런거 헷갈리지마라;;; 바보냐