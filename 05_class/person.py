class Person:
    count = 0       # 클래스 변수
    def __init__(self,name,age=1):      # 생성자
        self.name = name
        self.__age = age        # private
        Person.count += 1
        print(self.name + "(" + str(self.__age) + ") is initialized")

    def work(self,company):
        print(self.name + " is working in " + company)
        self.__getage()

    def sleep(self):
        print(self.name + " is sleeping")

    def __getage(self):     # private
        print(self.__age)

    @classmethod        # 클래스 메소드(annotation, 클래스에서 공통적으로 사용하는 메소드)
    def getCount(cls):      # cls : class(self 대신 cls 사용)
        return cls.count

################################################################

obj1 = Person("hong")
obj2 = Person("kim", 20)

obj1.work("abc")        # __getage() : class 내부에서 접근 가능
obj2.sleep()
# obj1.__getage()     # class 외부에서 접근 못함

print(obj1.name)
# print(obj1.__age)       # class 외부에서 접근 못함
print(obj1._Person__age)        # 접근 가능
print(obj2._Person__age)        # 접근 가능

print(obj1.getCount())
print(obj2.getCount())
print(Person.getCount())        # 클래스 변수는 이렇게 쓰는 것이 좋다
obj2.count = 8
print(obj2.count)     # 출력 : 8
print(obj2.getCount())      # 출력 : 2