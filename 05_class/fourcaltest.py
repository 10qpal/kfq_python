class FourCal:

    def __init__(self, first=1, second=4):
        self.first = first
        self.second = second
        print("생성자")

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

################################################################

class MoreFourCal(FourCal):     # 클래스 상속 : class 클래스 이름(상속할 클래스 이름)
    def pow(self):
        result = self.first ** self.second
        return result

    def div(self):      # 메소드 오버라이딩 : 부모 클래스에 있는 메소드를 다시 만드는 것
        if self.second == 0:
            print("0으로 나눌 수 없습니다.")
            return 0
        else:
            return self.first / self.second

cal1 = MoreFourCal(5,0)
cal2 = MoreFourCal(5,6)

print(cal1.add())       # 상속 확인
print(cal2.add())       # 상속 확인
print()
print(cal1.pow())
print(cal2.pow())
print()
print(cal1.div())
print(cal2.div())