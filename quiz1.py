# studentlist = []
studentlist = [["123","홍길동","기계공학","5555","대구광역시"],
["234","고길동","화학공학","3333","부산광역시"],
["345","김길동","전자공학","7777","서울특별시"],]

while True:

    choice=input('''
    ====================================
    학생 정보 프로그램입니다.
    다음 중에서 하실 일을 골라주세요 :
    C(c) - 학생 정보 입력
    R(r) - 학생 정보 출력
    U(u) - 학생 정보 수정
    D(d) - 학생 정보 삭제
    Q(q) - 프로그램 종료
    ====================================
    ''').upper()

    if choice == "C":
        print("학생 정보 입력")
        while True:
            num = input("학번을 입력하세요 >>> ")
            check = 0
            for i in range(0, len(studentlist)):
                if studentlist[i][0] == num:
                    check = 1
                    print("학번은 중복될 수 없습니다.")
            if check == 0:
                break
        name = input("이름을 입력하세요 >>> ")
        subject = input("학과를 입력하세요 >>> ")
        call = input("전화번호를 입력하세요 >>> ")
        address = input("주소를 입력하세요 >>> ")
        newstudent = [num, name, subject, call, address]

        studentlist.append(newstudent)
        # print(studentlist)
        print("학생 정보 입력 완료")

    elif choice == "R":
        print("학생 정보 출력")
        print("{:10} {:10} {:15} {:20} {:40}".format('학번','이름','학과','전화번호','주소'))
        for i in range(0, len(studentlist)):
            print("{:10} {:10} {:15} {:20} {:40}".format(studentlist[i][0], studentlist[i][1], studentlist[i][2], studentlist[i][3], studentlist[i][4]))
        print()

    elif choice == "U":
        print("학생 정보 수정")
        while True:
            update = input("정보를 수정하려는 학생의 학번을 입력하세요 >>> ")
            idx = -1
            for i in range(0, len(studentlist)):
                if studentlist[i][0] == update:
                    idx = i
            if idx == -1:
                print("등록되지 않은 학생입니다.")
                break
            updatemenu = input("""
            수정하실 정보를 입력하세요.
            학과    전화번호    주소
            (수정하실 정보가 없으면 exit 입력)
            """)
            if updatemenu == "학과":
                studentlist[idx][2] = input("수정할 학과를 입력하세요 >>> ")
                print("학생 정보 수정 완료")
                break
            elif updatemenu == "전화번호":
                studentlist[idx][3] = input("수정할 전화번호를 입력하세요 >>> ")
                print("학생 정보 수정 완료")
                break
            elif updatemenu == "주소":
                studentlist[idx][4] = input("수정할 주소를 입력하세요 >>> ")
                print("학생 정보 수정 완료")
                break
            elif updatemenu == 'exit':
                print("학생 정보 수정 종료")
                break
            else:
                print("존재하지 않는 정보입니다.")
                break

    elif choice == "D":
        print("학생 정보 삭제")
        delete = input("정보를 삭제하려는 학생의 학번을 입력하세요 >>> ")
        delok = 0
        for i in range(0, len(studentlist)):
            if studentlist[i][0] == delete:
                print("{} 학생의 정보가 삭제되었습니다.".format(studentlist[i][1]))
                del studentlist[i]
                print("학생 정보 삭제 종료")
                delok = 1
            if delok == 1:
                break
        if delok == 0:
            print("등록되지 않은 학생입니다.")

    elif choice == "Q":
        print("학생 정보 프로그램 종료")
        break