from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


chromedriver = '/Users/soinseong/Documents/workspace/python/chromedriver'
driver = webdriver.Chrome(chromedriver)

param1 = '정자역'  # input text로 받을 값

# 크롤링할 사이트 호출
driver.get("https://www.diningcode.com/list.php?query=" + param1)

cnt = 0


def moreData(cnt):
    checkelement = driver.find_element_by_id("div_list_more")
    while checkelement.is_displayed():
        elem = driver.find_element(By.CSS_SELECTOR, 'a.more-btn')
        cnt = cnt + 1
        elem.send_keys(Keys.ENTER)
    return cnt


print("상위 ", moreData(cnt), "건이 조회되었습니다.")


time.sleep(1)

zero = driver.find_elements_by_css_selector('#div_list > li')[1:]
for test in zero:
    try:
        print(test.find_element_by_class_name("btxt").text, " : ", test.find_element_by_class_name("stxt").text)
        print("컨셉은 [ ", test.find_element_by_class_name("ctxt").text, " ]")
        print("점수는 ", test.find_element_by_class_name("point").text)
        print("=================================")
    except NoSuchElementException:
        continue
# two = driver.find_element_by_class_name("stxt")
# one = driver.find_element_by_class_name("btxt")
# three = driver.find_element_by_class_name("ctxt")
# four = driver.find_element_by_class_name("point")
