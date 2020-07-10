prompt = '''--------------------
 커피 자판기 메뉴
--------------------
1. 커피 메뉴 입력
2. 커피 메뉴 삭제
3. 커피 만들기
4. 메뉴판
5. 종료
--------------------'''
menudic = {"아메리카노":2000, "카페라떼":2500, "카푸치노":2500}
while True:
    print(prompt)
    menu = input("메뉴 선택 >>> ")

    if menu == '1':
        print("커피메뉴를 추가합니다.")
        name = input("메뉴명 >>> ")
        price = int(input("가격 >>> "))
        menudic[name] = price
        print(menudic)
        print("{} 메뉴는 {:,}원입니다.".format(name, price))

    elif menu == '2':
        print("커피메뉴를 삭제합니다.")
        print(menudic)
        name = input("삭제할 메뉴명 >>> ")
        #del menudic[name]
        menudic.pop(name)
        print(menudic)

    elif menu == '3':
        print("커피자판기 시작")
        print(menudic)
        choicemenu = input("커피메뉴를 입력하세요. >>> ")
        # if choicemenu not in menudic:
        #     print("커피메뉴에 없는 음료입니다.")
        #     continue
        if menudic.get(choicemenu) == None:             # get 함수 : 값 없으면 None 출력
                print("커피메뉴에 없는 음료입니다.")
        inputmoney = int(input("금액을 입력하세요. >>> "))
        if menudic[choicemenu] > inputmoney:            # cf.값 없으면 오류 출력
            print("금액이 부족합니다.")
        else:
            print("{}가(이) 나왔습니다.".format(choicemenu))
            print("거스름돈 {}원을 받으세요.".format(inputmoney-menudic[choicemenu]))

    elif menu == '4':
        print("--------------------")
        print("--------메뉴--------")
        print("--------------------")
        for k, v in menudic.items():
            print("{:<7} {:>,}원".format(k, v))

    elif menu == '5':
        print("프로그램 종료")
        break