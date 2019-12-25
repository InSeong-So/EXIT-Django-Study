from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import requests


# h1, 맛집을 찾으려는 지역을 입력하세요.
param = '정자역'
url = 'https://www.diningcode.com/isearch.php?query=' + param

html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
category = soup.select(".category-menu > .list > li")

temp = []
for at in category:
    temp.append(at.find("a").text)
del temp[0]

print(temp)


# chromedriver = '/Users/soinseong/Documents/workspace/python/chromedriver'
chromedriver = 'D:/sisworkspace/python/chromedriver'
driver = webdriver.Chrome(chromedriver)

param1 = '정자역'  # input text로 받을 값

param2 = '%20' + '한식'

# 크롤링할 사이트 호출
driver.get("https://www.diningcode.com/list.php?query=" + param1 + param2)

cnt = 0


def moreData(cnt):
    checkelement = driver.find_element_by_id("div_list_more")
    while checkelement.is_displayed():
        elem = driver.find_element(By.CSS_SELECTOR, 'a.more-btn')
        cnt = cnt + 1
        elem.send_keys(Keys.ENTER)
    return cnt

cnt2 = moreData(cnt)

print("상위 ", cnt2, "건이 조회되었습니다.")


time.sleep(1)

temp = []
# zero = driver.find_elements_by_css_selector('#div_list > li')[1:]
zero = driver.find_elements_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li[(contains(@id, "ad-area"))=false]')
print("기록중=============================")
for test in zero:
    try:
        temp.append([test.find_element_by_class_name("btxt").text, test.find_element_by_class_name("stxt").text, test.find_elements_by_class_name("ctxt")[0].text, test.find_elements_by_class_name("ctxt")[1].text, test.find_element_by_class_name("point").text])
        print(temp)
    except NoSuchElementException:
        continue
print("==============================기록끝")

# 명시적으로 일정시간을 기다릴 수 있음 (10초 기다림)
time.sleep(1)

# 크롬 브라우저 닫기 가능함
driver.quit()