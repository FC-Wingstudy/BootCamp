# from urlib.parse import SplitResult
import requests
from bs4 import BeautifulSoup

# 메인 지역 검색 url
main_brunch_url = 'http://www.naturekitchen.co.kr/Store/StoreFind.aspx?Area=경기'

# 요청을 보내서 status확인하기
response = requests.get(main_brunch_url)

# BeautifulSoup에서 사용할 수 있도록 인코딩? 한다.
soup = BeautifulSoup(response.text, 'lxml')


# 마지막 페이지를 확인하기 위해서 span 안의 a태그를 뽑아옴
span = soup.select('span a')

# 빈리트스안에 찾은 값을 채워 넣고
page_no_list = []
for i in span:
    t = i.get_text()
    page_no_list.append(i.get_text())

# 마지막 값이 빈값이라서 마지막 값은 삭제해줌
page_no_list.pop()

page_max = int(page_no_list[-1])
print(page_max)

for i in range(page_max):
    page_number = i + 1
    params = {

    }
    url = f'http://www.naturekitchen.co.kr/Store/StoreFind.aspx?CurrentPage={page_number}&Area=%EC%84%9C%EC%9A%B8&Search='
    response = requests.get(url)

    result = response.text

    soup = BeautifulSoup(result, 'lxml')

    main_menu = soup.select('table.tbl_store > tbody > tr')[2:]

    # print(main_menu)
    for td_list in main_menu:
        name = td_list.select_one('td:nth-of-type(2)').get_text(strip=True)
        location = td_list.select_one('td:nth-of-type(3)').get_text(strip=True)
        tel = td_list.select_one('td:nth-of-type(4)').get_text(strip=True)

        print(name)
        print(location)
        print(tel)
if __name__ == "__main__":
    pass