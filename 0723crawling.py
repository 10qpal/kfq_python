from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

driver = webdriver.Chrome('./crawling/data/chromedriver')
crawling = []

def crawling_data_python(url):
    driver.get(url)
    html = driver.page_source
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')

    # 제목
    title = soup.select('h1.entry-title')[0].text
    # tags = soup.select('h1.entry-title')
    # tag = tags[0]
    # title = tag.text
    # print(title)

    # 공동 공부자 수
    costudent = soup.select('span.count')[0].text
    # print(costudent)

    # 좋아요 수(오픈튜토리얼스 내)
    fb_url = 'https://www.facebook.com/plugins/like.php?app_id=&channel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2fe557de6fd8c%26domain%3Dopentutorials.org%26origin%3Dhttps%253A%252F%252Fopentutorials.org%252Ff56005260e0ec%26relation%3Dparent.parent&container_width=0&height=20&href=https%3A%2F%2Fopentutorials.org%2Fcourse%2F3256&layout=button_count&locale=ko_KR&sdk=joey&send=true&show_faces=false&width=450'
    driver.get(fb_url)
    fb_html = driver.page_source
    fb_soup = BeautifulSoup(fb_html, 'html.parser')
   
    like = fb_soup.select('#u_0_3')[0].text
    like = int(like[:-1])
    # print(like)

    result = [title, costudent, like]
    return result

def crawling_data_java(url):
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 제목
    title = soup.select('h1.entry-title')[0].text

    # 공동 공부자 수
    costudent = soup.select('span.count')[0].text

    # 좋아요 수(오픈튜토리얼스 내)
    fb_url = 'https://www.facebook.com/plugins/like.php?app_id=&channel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df32fac5e23f018%26domain%3Dopentutorials.org%26origin%3Dhttps%253A%252F%252Fopentutorials.org%252Ff3822bf6246a608%26relation%3Dparent.parent&container_width=0&height=20&href=https%3A%2F%2Fopentutorials.org%2Fcourse%2F3930&layout=button_count&locale=ko_KR&sdk=joey&send=true&show_faces=false&width=450'
    driver.get(fb_url)
    fb_html = driver.page_source
    fb_soup = BeautifulSoup(fb_html, 'html.parser')
   
    like = fb_soup.select('#u_0_3')[0].text
    like = int(like[:-1]) + 153
    # print(like)

    result = [title, costudent, like]
    return result

def write_csv(crawling):
    with open('opentutorials.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in crawling:
            writer.writerow(row)



url_python = 'https://opentutorials.org/course/3256'
crawling.append(crawling_data_python(url_python))
url_java = 'https://opentutorials.org/course/3930'
crawling.append(crawling_data_java(url_java))


print(crawling)