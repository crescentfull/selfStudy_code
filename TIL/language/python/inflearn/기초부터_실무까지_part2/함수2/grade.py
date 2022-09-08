# grade 모듈

# 아래 함수는 사용자로부터 성적을 입력 받는다. 사용자가 음수를 입력하면
# 성적을 입력받는 것을 멈추도록 한다.

def readList():
    score_list = [] # 성적을 저장할 리스트
    flag = True      # 무한루프 종료위한 변수 boolean
    
    #무한루프
    while flag:
        score = int(input("성적을 입력하시오(종료는 음수 입력) : "))
        # 음수가 들어왔는지 체크를 하는 부분(무한루프 탈출 구간)
        if score < 0:
            flag = False # 종료
        else:
            score_list.append(score)  # 점수 추가
    return score_list

#입력받은 성적 오름차순 정렬
def sortingList(score_list):
    score_list.sort()
    return score_list

#오름차순 정렬된 
def show_case(score_list):
    j = 0
    for i in score_list:
        print((j+1),"번째 성적 : ", i)
        j += 1
    
    
