# 친구 목록 관리 프로그램

def friend_management():
    fr_list = []
    while True:
        print("1. 친구 리스트 출력")
        print("2. 친구 추가")
        print("3. 친구 삭제")
        print("4. 친구 이름 변경")
        print("9. 종료\n")
        menu_num = int(input("메뉴를 선택하세요: "))
        
        if menu_num == 1:
            print(fr_list)
        elif menu_num == 2:
            fr_name = input("추가할 친구 이름을 입력하세요: ")
            fr_list.append(fr_name)
        elif menu_num == 3:
            fr_name = input("삭제할 친구 이름을 입력하세요: ")
            fr_list.remove(fr_name)
        elif menu_num == 4:
            original_name = input("변경하고 싶은 친구 이름을 입력하세요: ")
            new_name = input("새로운 이름을 입력하세요: ")
            fr_list[fr_list.index(original_name)] = new_name
        else:
            print("프로그램이 종료되었습니다.")
            break
if __name__ == "__main__":
    friend_management()