str1 = 'abcdef'
list1 = [1, 2, 3, 4, 5, 6]
tuple1 = (1, 2, 3, 4, 5, 6)
dic1 = {1:"첫번째", 2:"두번째"}
set1 = {1, 2, 3}

# for i in set1:
#     print(i, end=",")
# print("")
# for k, v in dic1.items():           # .items() : 한 쌍의 정보를 list로 return, .keys(), .values()
#     print(k, v)
# print("")
# for i in range(1, 10):              # 1부터 9까지
#     print(i)

# 구구단
# for i in range(2, 10):
#     print("[%d단]" %i)
#     for j in range(1, 10):
#         print("%d X %d = %2d" %(i, j, i*j))
# print()
# for j in range(1, 10):
#     for i in range(2, 10):
#         print("{} X {} = {:2}".format(i, j, i*j), end="   ")
#     print()
# print()

# 리스트 내포
a = [1, 2, 3, 4, 5]
result = [num*3 for num in a if num % 2 == 0]
print(result)

result = []
for num in a:
    if num%2 == 0:
        result.append(num*3)
print(result)