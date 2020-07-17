from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('./crawling/data/chromedriver')

url = 'https://nid.naver.com/nidlogin.login'
driver.get(url)
driver.implicitly_wait(3)       # time.sleep(10) 대신 사용 가능

id = 'ysc_akdhkd@naver.com'
pw = 'cutthebeat@2'

# driver.find_element_by_name('id').send_keys(id)
# driver.find_element_by_name('pw').send_keys(pw)
# submit = driver.find_element_by_id('log.login')
# submit.click()

driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
time.sleep(5)

# element 창 로그인 버튼 소스 선택된 상태에서 마우스 오른쪽 버튼 클릭 - copy - copy XPath
driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(5)

# 처음 로그인했을 때 등록할 것인지 묻는다
# driver.find_element_by_xpath('//*[@id="new.save"]').click()
# time.sleep(5)

# 네이버 페이 들어가기(URL로)
# url = 'https://order.pay.naver.com/home'
# driver.get(url)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# point = soup.select_one('dl.my_npoint strong')
# print(point.string)
# time.sleep(5)

# 네이버 메일 들어가서 메일 보낸 사람, 제목 출력하기(클릭으로)
mail = driver.find_element_by_class_name('nav')
mail.click()
time.sleep(5)

mtitle = driver.find_element_by_class_name('mTitle')
print(mtitle.text)
