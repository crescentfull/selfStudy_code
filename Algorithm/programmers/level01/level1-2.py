'''
[평균 구하기]
# 문제 설명
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# 제한사항
arr은 길이 1 이상, 100 이하인 배열입니다.
arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

## 입출력 예
arr       | return
[1,2,3,4] | 2.5
[5,5]     | 5
'''
arr = [1,2,3,4]
def solution(arr):
    answer = 0
    return sum(arr)/len(arr) 
#sum() list나 tuplec처럼 인자가 숫자로만 이루어져 있는 배열에 사용, 원소값 합계구해주는 함수
#len() 배열의 길이 arr가 4개의 원소를 가지고 있으므로 길이는 4
