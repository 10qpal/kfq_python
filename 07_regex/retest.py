import re
# p = re.compile('ab*')

# # match : 처음부터 비교
# m1 = p.match("ac")       # 매치가 되면 match 객체 돌려준다
# m2 = p.match("bac")      # 매치가 안 되면 None 돌려준다
# print(m1)
# print(m2)

# # search :
# s1 = p.search("abbbc")       # 서치가 되면 match 객체 돌려준다
# s2 = p.search("babbbc")      # 서치가 안 되면 None 돌려준다
# #s2 = re.search('ab*','babbbc')
# print(s1)
# print(s2)

email = input("이메일 입력 : ")
p = re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}.[a-z]{2,5}')
# 소문자 1자리 + 소문자or숫자 4자리(최소 5자리 이상)
result = p.match(email)
print(result)