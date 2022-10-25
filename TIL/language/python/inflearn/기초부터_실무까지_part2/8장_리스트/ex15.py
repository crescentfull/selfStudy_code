# 탐색하기
# 주어진 데이터 내에서 어떠한 특정 값을 찾는 행위가 탐색 하는 것
# index()를 이용하여 일반적인 탐색이 가능하다

list_word = ["gold","blue","red","yellow","green"]
search_word = input("찾을 단어 입력 : ")

if search_word in list_word:
    index = list_word.index(search_word)+1
    print(f"단어 {index}번쨰에 존재합니다")
else:
    print("찾고자 하는 단어가 없습니다.")
    
# 프로그래머가 직접 탐색을 구현해야하는 경우도 많다.
# 탐색의 가장 기본적인 방법이 순차 탐색이다.
# 순차 탐색은 리스트의 요소를 순서대로 하나씩 꺼내서 비교해서 성공하면,
# 루프를 빠져나오고 루프를 다 했음에도 없다면 탐색키가 존재하지 않음을 의미한다.
def num_search(list, key):
    cnt = 0 # 숫자 카운트 초기화
    for i in range(len(list)):
        if key == list[i]:
            cnt += 1
    return cnt

num_list = [10,20,30,40,50,60,70,70,70,70,70]
key = int(input("숫자를 입력하시오 : "))
cnt = num_search(num_list, key)

if cnt == 0:
    print(key,"은 존재하지 않습니다.")
else:
    print(f"{key}은(는) {cnt}개 존재합니다.")

# 모든 조건에 만족하는 항목을 전부 찾는 방법
result = []
for i in num_list:
    if i >= 50:
        result.append(i)
print(result,len(result))

# 사용자로부터 키를 입력받아서 키값 이상의 값들을 출력하고 
# 그 키값 이상인 값들의 총 갯수를 구하는 프로그램을 작성
num_key = int(input("숫자를 입력하세요 : "))
res = []
for i in num_list:
    if i >= num_key:
        res.append(i)
print(res)
