# class Cookie:
#     pass

# a = Cookie()

# print(type(a))

class FourCal:
    mode = 1        # 클래스 변수, 초기값 없으면 안 만들어진다
    # def __init__(self):      # 생성자(이름이 __init__로 정해져 있다)
    #     print("생성자")

    def __init__(self, first=1, second=4):      # 생성자(초기값을 넣어줄 수도 있다) 
        self.first = first
        self.second = second
        print("생성자")

    def setdata(self, first, second):       # 첫번째 인자는 무조건 self, 선언은 하지만 사용하지는 않는다
        self.first = first      # 매개변수(지역변수) -> self가 붙으면 전역변수가 된다
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

# a = FourCal()
# a.setdata(3, 6)
# result = a.add()
# print(result)
# print(a.first)
# print(id(a.first))

# b = FourCal()
# b.setdata(2, 4)
# print(b.first)
# print(id(b.first))

# a = FourCal()       # 기본값 있으면 안 넣어줘도 되고
# b = FourCal(4, 7)

a = FourCal(1, 2)
b = FourCal(2, 3)
c = FourCal(3, 4)

print(FourCal.mode)
print(a.mode)
print(b.mode)
print(c.mode)
print(id(FourCal.mode))
print(id(a.mode))
print(id(b.mode))
print(id(c.mode))
print()

FourCal.mode = 11
print(FourCal.mode)
print(a.mode)
print(b.mode)
print(c.mode)
print(id(FourCal.mode))
print(id(a.mode))
print(id(b.mode))
print(id(c.mode))
print()

a.mode = 10
print(FourCal.mode)
print(a.mode)
print(b.mode)
print(c.mode)
print(id(FourCal.mode))
print(id(a.mode))
print(id(b.mode))
print(id(c.mode))
print()