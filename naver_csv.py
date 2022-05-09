from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import csv

#브라우저 생성
browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

#웹사이트 열기
browser.get('https://www.naver.com/')

#로딩 10초까지 대기
browser.implicitly_wait(10)

#쇼핑 메뉴 클릭하기
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2)

#검색창 클릭
search = browser.find_element_by_css_selector('input.co_srh_input._input')
search.click()

#검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

before_h = browser.execute_script("return window.scrollY")

#무한 스크롤
while True:
    browser.find_element_by_css_selector("body").send_keys(Keys.END)
    time.sleep(1)

    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

#파일 생성
f = open(r"C:\Users\jey28\Desktop\js\webTest\data.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)

#상춤 정보 duv
items = browser.find_elements(By.CSS_SELECTOR, ".basicList_info_area__17Xyo")

for item in items:
    name = item.find_element(By.CSS_SELECTOR, ".basicList_title__3P9Q7").text
    try:
        price = item.find_element(By.CSS_SELECTOR, "div.basicList_price_area__1UXXR > strong > span > span.price_num__2WUXn").text
    except:
        price = "price null"
    link = item.find_element(By.CSS_SELECTOR, ".basicList_title__3P9Q7 > a").get_attribute('href')
    print(name, price, link)
    csvWriter.writerow([name, price, link])

f.close()