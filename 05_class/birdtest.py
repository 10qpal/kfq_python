# class Bird:
#     def fly(self):
#         raise NotImplementedError       # 오류 발생

# # b = Bird()
# # b.fly()

# class B(Bird):      # 상속
#     def fly(self):
#         print("fly")

# b1 = B()
# b1.fly()

class MyError(Exception):       # Exception 상속받아서 예외 만드는 클래스 생성
    def __str__(self):
        return "부적절한 별명"      # 오류 메시지 출력됨(print("부적절한 별명")과 같은 동작)

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

try:
    say_nick("바보11")
    say_nick("바보")
    say_nick("바보22")
except MyError as err:
    print(err)