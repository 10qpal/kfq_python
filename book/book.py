

booklist=[{'booknum':1,'title':'murder','publisher':'kfq','author':'hwang','description':'how to kill a person','ea':60},
{'booknum':2,'title':'falling airplane','publisher':'England','author':'Johnson','description':'why?why?why?why?why?','ea':100},
{'booknum':3,'title':'paper lady','publisher':'France','author':'GM','description':'romantic','ea':10}]
idx = 3
same = 0

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    L - 책 목록  
    A - 책 등록
    U - 책 정보 수정
    B - 책 대여
    D - 책 삭제
    Q - 프로그램 종료
    ''').upper()

    if choice=="L":
        print("책 목록")
        print("{:3} {:20} {:15} {:10} {:40} {:10}".format('no','title','publisher','author','description','ea'))
        for i in booklist:
            print("{:>3} {:20} {:15} {:10} {:40} {:<10}".format(i['booknum'],i['title'],i['publisher'],i['author'],i['description'],i['ea']))
        print()

    elif choice=="A":
        print("책 등록")
        while True:
            same = 0 
            book = {'booknum':'', 'title':'', 'publisher':'','author':'','description':'','ea':''}
            book['booknum'] = int(idx+1)
            book['title'] = str(input("책 제목을 입력하세요. : "))

            for i in booklist:
                if i['title'] == book['title']:
                    print("같은 이름의 책이 있습니다.")
                    same = 1
                    add = input("추가 수량을 입력하세요. ")
                    if add.isdecimal():
                        add = int(add)
                        i['ea']+=add
                        break
                    else:
                        print("숫자를 입력하세요.")
            if same == 0:
                book['publisher'] = str(input("출판사를 입력하세요. : "))
                book['author'] = str(input("저자를 입력하세요. : "))
                book['description'] = str(input("설명을 입력하세요. : "))
                while True:
                    book['ea'] = str(input("재고를 입력하세요. : "))
                    if book['ea'].isdecimal():
                        book['ea'] = int(book['ea'])
                        break
                    else:
                        print("숫자를 입력하세요.")

                booklist.append(book)
                idx+=1

            print("{:3} {:20} {:15} {:10} {:40} {:10}".format('no','title','publisher','author','description','ea'))
            for i in booklist:
                print("{:>3} {:20} {:15} {:10} {:40} {:<10}".format(i['booknum'],i['title'],i['publisher'],i['author'],i['description'],i['ea']))
            print()
            break

    elif choice=="U":
        print("고객 정보 수정")
        print("{:3} {:20}".format('no','title'))
        for i in booklist:
            print("{:>3} {:20}".format(i['booknum'],i['title']))
        print()

        while True:
            updatebook = input("수정하려는 책의 제목을 입력하세요. : ")
            page = -1
            for i in range(0, len(booklist)):
                if booklist[i]['title'] == updatebook:      # i번째, 키 값(이메일)
                    page = i
            if page == -1:
                print("목록에 없는 책입니다.")
                break
            updatemenu = input("""
            다음 중 수정하실 정보를 입력하세요.
            publisher, author, description
            (수정할 정보가 없으면 exit 입력)
            """)
            if updatemenu in ('publisher', 'author', 'description'):
                booklist[page][updatemenu] = input("수정할 {}을 입력하세요. : ".format(updatemenu))
                for i in booklist:
                    print(i['title'],end="   ")
                print()
                break
            elif updatemenu == 'exit':
                break
            else:
                print("존재하지 않는 정보입니다.")
                break

    elif choice=="B":
        print("{:3} {:20} {:10}".format('no','title', 'ea'))
        for i in booklist:
            print("{:>3} {:20} {:<10}".format(i['booknum'],i['title'],i['ea']))
        print()

        while True:
            updatebook = input("대여하려는 책의 제목을 입력하세요. : ")
            page = -1
            for i in range(0, len(booklist)):
                if booklist[i]['title'] == updatebook:      # i번째, 키 값(이메일)
                    page = i
            if page == -1:
                print("목록에 없는 책입니다.")
                break
            while True:
                borrow = str(input("대여할 수량을 입력하세요. : "))
                if borrow.isdecimal():
                    borrow = int(borrow)
                    imsi = booklist[page]['ea'] - borrow
                else:
                    print("숫자를 입력하세요.")

                if imsi < 0:
                    print("대여할 수량이 재고보다 많습니다. 다시 입력하세요.")
                else:
                    booklist[page]['ea'] = imsi
                    break
            if imsi >= 0:
                break

                
        print("{:3} {:20} {:10}".format('no','title', 'ea'))
        for i in booklist:
            print("{:>3} {:20} {:<10}".format(i['booknum'],i['title'],i['ea']))
        print()

    elif choice=="D":
        print("책 삭제")
        print("{:3} {:20}".format('no','title'))
        for i in booklist:
            print("{:>3} {:20}".format(i['booknum'],i['title']))
        print()

        delete = input("삭제하려는 책의 제목을 입력하세요. : ")
        delok = 0
        for i in range(0, len(booklist)):
            if booklist[i]['title'] == delete:
                print("{} 책의 정보가 삭제되었습니다.".format(booklist[i]['title']))
                del booklist[i]
                delok = 1
            if delok == 1:
                break
        if delok == 0:
            print("목록에 없는 책입니다.")

    elif choice=="Q":
        print("프로그램 종료")
        break