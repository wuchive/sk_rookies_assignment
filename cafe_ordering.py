# 카페 주문 관리 프로그램

def cafe_ordering():
    menu_dict = {"아메리카노": 4000, "카페라떼": 5000, "카페모카": 6000}
    order_list = []
    total_value = 0
    menu = """
    아메리카노: 4000원
    카페라떼: 5000원
    카페모카: 6000원
        
    """
    print(menu)

    while True:
        new_order = input("주문할 메뉴를 입력하세요 (종료: 'q): ")
        if new_order in menu_dict:
            order_list.append(new_order)
        if new_order == "아메리카노":
            total_value += menu_dict["아메리카노"]
        elif new_order == "카페라떼":
            total_value += menu_dict["카페라떼"]
        elif new_order == "카페모카":
            total_value += menu_dict["카페모카"]
        elif new_order == "q":
            if len(order_list) == 0:
                return
            else:
                input_money = int(input(f"총 금액은 {total_value}원입니다. 돈을 넣으세요: "))
                break
        else:
            print("메뉴가 없습니다. 다시 입력하세요.")
        
        
    print(order_list)
    change_money = input_money - total_value
    if change_money < 0:
        print("돈이 부족합니다.")
    else:
        print(f"{len(order_list)}개 구매 완료. 거스름돈은 {change_money}원입니다.")
        
if __name__ == "__main__":
    cafe_ordering()