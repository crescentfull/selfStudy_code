'''
함수 solution은 정수 n을 매개변수로 입력받습니다. 
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
예를들어 n이 118372면 873211을 리턴하면 됩니다.

##제한조건
n은 1이상 8000000000 이하인 자연수입니다.

## 입출력 예
n      = 118372
return = 873211
'''
n = 12398764
def solution(n):
    answer = 0
    #input값을 리스트로 변환
    res = list(str(n)) #list()함수 사용, imutable을 위해서 input값 문자열로 변경위해 str() 사용
    res.sort(reverse = True) #리스트로 받고 정렬 함수 sort()에서 reverse로 역순으로 재정렬
    answer = ''.join(res) # 역순으로 정렬된 문자열 배열을 하나의 문자열로 합치기위해 ''.join() 사용 
    print(int(answer)) 
    return int(answer) #답은 int형으로 나와야하기 때문에 return 값 int()로 치환

solution(n)