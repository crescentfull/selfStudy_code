# 한사람이 돈이 5000원이 있는데 사탕의 가격기 120원이라면 최대로 살 수 있는 사탕의 갯수는?

myMoney = 5000
candyPrice = 120

# 최대로 살 수 있는 사탕의 갯수
numCandies = myMoney // candyPrice
# / => 실수 , // => 정수
print("최대로 살 수 있는 사탕의 갯수 : ", numCandies)
# 구입하고 남은 돈

change = myMoney % candyPrice # % => 나머지
print("최대로 살 수 있는 사탕을 구입하고 남은 돈 : ", change)