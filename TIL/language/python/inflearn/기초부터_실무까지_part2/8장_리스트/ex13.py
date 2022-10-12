# 연락처 관리 프로그램
# 출력결과
# -----------------
# 1. 친구리스트 출력
# 2. 친구추가
# 3. 친구삭제
# 4. 이름변경
# 0. 종료
# 메뉴 선택 :
# 이름 입력 :
# -----------------
# 1. 친구리스트 출력
# 2. 친구추가
# 3. 친구삭제
# 4. 이름변경
# 0. 종료
# 메뉴를 선택하시오 : 

def menu_print():
    print("1. 친구리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("0. 종료")

menu_choice = 0 # 메뉴 번호를 저장
friends = []    # 친구 목록을 리스트에 저장

while True:
    menu_print()
    menu_choice = int(input("메뉴 선택 : "))
    
    # 종료
    if menu_choice == 0:
        print("프로그램을 종료합니다")
        break
    elif menu_choice == 1:
        print("친구목록 : ", friends)
    elif menu_choice == 2:
        add = input("친구 이름을 입력 : ")
        friends.append(add)
    elif menu_choice == 3:
        del_friend = input("삭제할 친구 이름 입력 : ")
        if del_friend in friends:
            friends.remove(del_friend)
        else:
            print("친구가 없어요")
    elif 