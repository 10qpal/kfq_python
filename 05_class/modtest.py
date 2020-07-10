# import mod1       # 전체 호출

# a = mod1.add(4,2)
# print(a)

# from mod1 import add      # 쓰려고 하는 부분만 호출

# a = add(4,2)
# print(a)

# from mod.mod1 import add,sub        # 경로가 다를 때 접근(1)

# a = add(4,2)
# print(a)
# b = sub(4,2)
# print(b)

# from mod import mod1        # 경로가 다를 때 접근(2)

# a = mod1.sub(4,2)
# print(a)

from mod import mod1 as m       # 별칭 만들기

a = m.add(4,2)
print(a)
b = m.sub(4,2)
print(b)

import sys
print(sys.path)

# from mtest import mod2     # 실행 안됨
# print(mod2.div(4,2))

sys.path.append('C:\\code\\gitdata\\pythoncode\\mtest')     # 경로 등록
import mod2
print(mod2.div(4,2))
