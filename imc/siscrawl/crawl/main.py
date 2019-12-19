import requests
from bs4 import BeautifulSoup


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



# h2, 원하시는 카테고리를 선택하세요.
url2 = 'https://www.diningcode.com/isearch.php?query=' + param + '%20' + temp[1]


# h3, 맛집 리스트를 출력합니다.
text1 = soup.findAll("span", attrs={"class":"btxt"})
text2 = soup.findAll("span", attrs={"class":"stxt"})

for line1, line2 in zip(text1[1:], text2[1:]):
    print(line1.get_text(), end= ': ')
    print(line2.get_text())

