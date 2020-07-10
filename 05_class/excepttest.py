#FileNotFoundError
# f = open("./05_class/classtest.txt", "r")

#ZeroDivisionError
# 4/0       

#IndexError
# li = [1,2,3]
# li[4]

try:
    4/1
    4/0
    f = open("./05_class/classtest.txt", "r")
    li = [1,2,3]
    li[4]
except IndexError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
except FileNotFoundError as err:
    pass
finally:
    print("finally")