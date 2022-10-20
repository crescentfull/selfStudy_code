# 일반적인 리스트 연산 연습
# 최솟값 최댓값을 구하는 알고리즘

num = [1, 5, -9, 100]
print("최솟값 : ", min(num))
print("최댓값 : ", max(num))

# 최대값과 최소값을 구하는 알고리즘은 상당히 중요한 개념, 
prices = [1000, 3000, 500, 10000, 20000, 700]

# 먼저 prices[]에 있는 0번째 인덱스 값을 변수에 저장을 한다.
lowPrice = prices[0]
# 이후, 루프를 돌면서 조건식으로 값이 작으면 해당하는 값을 lowPrice변수에 재저장
#최소값
for i in range(1,len(prices)): #0번 인덱스를 이미 사용하므로 굳이 cpu사용을 높일 이유가 없다.
    if prices[i] < lowPrice: # 참, prices[i]가 lowPrice 보다 작다라는 의미
        lowPrice = prices[i]
print("가장 싼 가격 : ", lowPrice)
#최대값        
for i in range(1,len(prices)): #0번 인덱스를 이미 사용하므로 굳이 cpu사용을 높일 이유가 없다.
    if prices[i] > lowPrice: # 참, prices[i]가 lowPrice 보다 크다라는 의미
        lowPrice = prices[i]
print("가장 비싼 가격 : ", lowPrice)
#부등호만 바꾸면 된다.

# 문자열에서 가장 짧은 문자열을 구하는 알고리즘 코드
words = ['dog','cat','horse','lion','tiger','eagle','elephant']
word_han = ['안녕','하이','반갑습니다','가세요','오랜만입니다']
# 제일 짧은 문자열
print("가장 짧은 단어 : ", min(words)) # >>> cat 
# 왜 cat? askii 코드값으로 가져오기 때문이다.
print("가장 긴 단어 : ", max(words))
print("가장 짧은 단어 : ", min(word_han))
print("가장 긴 단어 : ", max(word_han))

# 문자열에서 가장 짧은 문자열을 구하는 알고리즘 코드
shortest_word = words[0]