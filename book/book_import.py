import bookfunc

booklist=[{'booknum':1,'title':'murder','publisher':'kfq','author':'hwang','description':'how to kill a person','ea':60},
{'booknum':2,'title':'falling airplane','publisher':'England','author':'Johnson','description':'why?why?why?why?why?','ea':100},
{'booknum':3,'title':'paper lady','publisher':'France','author':'GM','description':'romantic','ea':10}]
idx = 3
same = 0

def exe(choice, idx):
    if choice=='L':
        bookfunc.blist(booklist)
    elif choice=='A':
        idx = bookfunc.add(booklist, idx)
    elif choice=='U':
        bookfunc.update(booklist)
    elif choice=='B':
        bookfunc.borrow(booklist)
    elif choice=='D':   
        bookfunc.delete(booklist)             
    elif choice=='Q':
        quit()   
    return idx

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

    idx = exe(choice, idx)