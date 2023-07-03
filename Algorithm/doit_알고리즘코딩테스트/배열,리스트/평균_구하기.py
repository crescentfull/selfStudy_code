'''

세준이는 기말고사를 망쳤다. 그래서 점수를 조작해 집에 가져가기로 결심했다. 일단 세준이는 자기 점수중 최댓값을 골랐다.
그런 다음 최댓값을 M이라 할 때 모든 점수를 점수 / M * 100으로 고쳤다. 예를 들어 세준이의 최고점이 70점, 수학 점수가 50점이라면 
수학 점수는 50/70 * 100이므로 71.43 점이다.
세준이의 성적을 이 방법으로 계산 했을때 새로운 평균을 구하는 프로그램을 작성하시오.

# 입력
1번째 줄에 시험을 본 가목의 개수 N이 주어진다. 해당값은 1,000보다 작거나 같다. 2번째 줄에 세준이의 현재 성적이 주어진다.
해당 깂은 100보다 작거나 같은, 음이 아닌 정수이고, 적어도 1개의 값은 0보다 크다.

# 출력
1번째 줄에 새로운 평균을 출력한다.
실제 정답과 출력 값의 절대 오차 또는 상대 오차가 10^-2이하이면 정답이다.

입력1
3
40 80 60
출력1
75.0

입력2
3
10 20 30
출력2
66.666667
'''

# n = list(input("값").split())
# n = [int(i) for i in n]
# print(n)

# max_num = max(n)
# print(round((sum(n)*100)/max_num/3,6))

n = input()
myList = list(map(int, input().split()))
myMax = max(myList)
sum = sum(myList)
print(round(sum*100/ myMax / int(n),6))