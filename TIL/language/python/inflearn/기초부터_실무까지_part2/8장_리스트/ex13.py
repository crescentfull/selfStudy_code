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
    print("*********************************")
    print("1. 친구리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("0. 종료")

menu_choice = 0 # 메뉴 번호를 저장
friends = []    # 친구 목록을 리스트에 저장
mobile = [] # 전화번호

while False:
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
    elif menu_choice == 4:
        old_name = input("변경을 원하는 이름 입력 : ")
        if old_name in friends:
            index = friends.index(old_name) # 변경할 이름의 인덱스를 가져온다
            new_name = input("새로운 이름을 입력하세요 : ")
            friends[index] = new_name
        else:
            print(old_name,"이름 없음")
            
# 친구추가시 연락처도 함께 업데이트 하는 프로그램
while True:
    menu_print()
    menu_choice = int(input("메뉴 선택 : "))
    
    # 종료
    if menu_choice == 0:
        print("프로그램을 종료합니다")
        break
    elif menu_choice == 1:
        print("친구 목록 : ", friends)
        print("번호 목록 : ", mobile)
    elif menu_choice == 2:
        add = input("친구 이름을 입력 : ")
        friends.append(add)
        add_mobile = input("전화 번호 입력 : ")
        mobile.append(add_mobile)
    elif menu_choice == 3:
        del_friend = input("삭제할 친구 이름 입력 : ")
        index_mobile = friends.index(del_friend)
    
        if del_friend in friends:
            friends.remove(del_friend)
            mobile.remove(mobile[index_mobile])
        else:
            print("친구가 없어요")
    elif menu_choice == 4:
        old_name = input("변경을 원하는 이름 입력 : ")
        if old_name in friends:
            index = friends.index(old_name) # 변경할 이름의 인덱스를 가져온다
            new_name = input("새로운 이름을 입력하세요 : ")
            friends[index] = new_name
            new_mobile = input("새로운 번호를 입력 : ")
            mobile[index] = new_mobile
        else:
            print(old_name,"이름 없음")