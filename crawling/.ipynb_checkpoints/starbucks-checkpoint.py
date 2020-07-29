from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('./crawling/data/chromedriver')

url = 'https://www.starbucks.co.kr/store/store_map.do'
driver.get(url)
time.sleep(10)      # 10sec

source = driver.page_source
# print(type(source))       # type : str
soup = BeautifulSoup(source, 'html.parser')
# print(soup.select('li.quickResultLstCon'))

loca = driver.find_element_by_class_name('loca_search')     # 클래스 이름으로 찾음
loca.click()        # 클릭 이벤트
time.sleep(10)

sido = driver.find_element_by_class_name('sido_arae_box')
li = sido.find_elements_by_tag_name('li')       # find_elements <- s 확인(여러 개 리턴)
# print(type(li))
li[3].click()       # list : index로 접근 가능
time.sleep(10)

gugun = driver.find_element_by_class_name('gugun_arae_box')
li = gugun.find_elements_by_tag_name('li')       # find_elements <- s 확인(여러 개 리턴)
li[8].click()       # list : index로 접근 가능
time.sleep(10)

source = driver.page_source

bs = BeautifulSoup(source, 'html.parser')
entire = bs.find('ul', class_= 'quickSearchResultBoxSidoGugun')
li_list = entire.find_all('li')

for li in li_list:
    print(li.find('strong').text + " / " + li.find('p').text)