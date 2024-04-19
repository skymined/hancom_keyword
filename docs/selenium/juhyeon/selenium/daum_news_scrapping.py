# * 웹 크롤링 동작
from selenium import webdriver 
import time
# ChromeDriver 실행
# Chrome WebDriver의 capabilities 속성 사용
# capabilities = browser.capabilities

browser = webdriver.Chrome()                        # - chrome browser 열기
pass

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)



from selenium.webdriver.chrome.options import Options

from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://192.168.10.240:27017/")
# database 연결
database = mongoClient["local"]
# collection 작업   
collection = database['daum_news']
# insert 작업 진행
collection.delete_many({})

# ChromeDriver 실행
url = 'https://search.daum.net/search?w=news&nil_search=btn&DA=STC&enc=utf8&cluster=y&cluster_page=1&q=%ED%95%9C%EA%B8%80%EA%B3%BC+%EC%BB%B4%ED%93%A8%ED%84%B0&sd=20200101000000&ed=20211231235959&period=u&sort=old'
# url = 'https://search.daum.net/search?w=news&nil_search=btn&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%ED%95%9C%EA%B8%80%EA%B3%BC+%EC%BB%B4%ED%93%A8%ED%84%B0&sd=20200101000000&ed=20200104235959&period=u&sort=old&p=1'
pass
browser.get(url)           # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
time.sleep(3)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
date_choose_btn = browser.find_element(by=By.CSS_SELECTOR,value="div#daumContent div.inner_article > div.g_comp > div#dnsColl > div:nth-child(1) > div.c-filter.ty_etc.comp_fold > div.c-option > div:nth-child(2) > div.c-sub-sort > a:nth-child(7)")
btn_year_list = [browser.find_element(by=By.CSS_SELECTOR,value='div:nth-child(1) > div > label:nth-child(31) > input'),browser.find_element(by=By.CSS_SELECTOR,value='div:nth-child(1) > div > label:nth-child(32) > input')]
for j in range(len(btn_year_list)):
    date_choose_btn = browser.find_element(by=By.CSS_SELECTOR,value="div#daumContent div.inner_article > div.g_comp > div#dnsColl > div:nth-child(1) > div.c-filter.ty_etc.comp_fold > div.c-option > div:nth-child(2) > div.c-sub-sort > a:nth-child(7)")
    btn_month_list = browser.find_elements(by=By.CSS_SELECTOR,value='div:nth-child(2) > div > label > input')
    for k in range(len(btn_month_list)):
        element_body = browser.find_element(by=By.CSS_SELECTOR,value='body.daum')
        element_body.send_keys(Keys.HOME)
        time.sleep(1)
        date_choose_btn = browser.find_element(by=By.CSS_SELECTOR,value="div#daumContent div.inner_article > div.g_comp > div#dnsColl > div:nth-child(1) > div.c-filter.ty_etc.comp_fold > div.c-option > div:nth-child(2) > div.c-sub-sort > a:nth-child(7)")
        date_choose_btn.click()
        start_date = browser.find_element(by=By.CSS_SELECTOR,value='div.date_selected > button.btn_set.focused')
        start_date.click()
        btn_year_list = [browser.find_element(by=By.CSS_SELECTOR,value='div:nth-child(1) > div > label:nth-child(31) > input'),browser.find_element(by=By.CSS_SELECTOR,value='div:nth-child(1) > div > label:nth-child(32) > input')]
        btn_year_list[j].click()
        btn_month_list = browser.find_elements(by=By.CSS_SELECTOR,value='div:nth-child(2) > div > label > input')
        btn_month_list[k].click()
        btn_day_list = browser.find_elements(by=By.CSS_SELECTOR,value=' div:nth-child(3) > div > label > input')
        btn_day_list[0].click()
        end_date = browser.find_element(by=By.CSS_SELECTOR,value='div.date_selected > button.btn_set.dimmed')
        end_date.click()
        btn_year_list = [browser.find_element(by=By.CSS_SELECTOR,value='div:nth-child(1) > div > label:nth-child(31) > input'),browser.find_element(by=By.CSS_SELECTOR,value='div:nth-child(1) > div > label:nth-child(32) > input')]
        btn_year_list[j].click()
        btn_month_list = browser.find_elements(by=By.CSS_SELECTOR,value='div:nth-child(2) > div > label > input')
        btn_month_list[k].click()
        btn_day_list = browser.find_elements(by=By.CSS_SELECTOR,value=' div:nth-child(3) > div > label > input')
        btn_day_list[-1].click()
        btn_apply = browser.find_element(by=By.CSS_SELECTOR,value='div.opt_detail.on > div > button')
        btn_apply.click()
        page_num = 0
        while True:
            if page_num != browser.find_element(by=By.CSS_SELECTOR,value='#dnsColl > div:nth-child(2) > div > div > em').text:
                page_num =  browser.find_element(by=By.CSS_SELECTOR,value='#dnsColl > div:nth-child(2) > div > div > em').text
            else:
                break
            next_btn = browser.find_element(by=By.CSS_SELECTOR,value='#dnsColl > div:nth-child(2) > div > button.btn_next')
            news_link_list = browser.find_elements(by=By.CSS_SELECTOR,value=" div.c-item-content > div.item-bundle-mid > div.item-title > strong > a")
            current_window_handle = browser.current_window_handle
            for news_link in news_link_list:
                current_window_handle = browser.current_window_handle
                news_link.click()
                window_handles = browser.window_handles
                browser.switch_to.window(window_handles[-1])
                time.sleep(1)
                pass

                news_brand = browser.find_element(by=By.CSS_SELECTOR,value="#kakaoServiceLogo")
                news_title = browser.find_element(by=By.CSS_SELECTOR,value="#mArticle > div.head_view > h3")
                news_date = browser.find_elements(by=By.CSS_SELECTOR,value="#mArticle > div.head_view > div.info_view > span > span")[-1]
                news_contents_list_p = browser.find_elements(by=By.CSS_SELECTOR,value='#mArticle > div.news_view.fs_type1 > div.article_view > section > p')
                news_contents_list_div = browser.find_elements(by=By.CSS_SELECTOR,value='#mArticle > div.news_view.fs_type1 > div.article_view > section > div')

                news_contents = ''
                for news_content in news_contents_list_p:
                    news_contents = news_contents + news_content.text + ' '
                for news_content in news_contents_list_div:
                    news_contents = news_contents + news_content.text + ' '
                print(news_brand.text)
                print(news_title.text)
                print(news_date.text)
                print(news_contents)
                collection.insert_one({'news_title': news_title.text,
                               'news_date':news_date.text,
                               'news_brand': news_brand.text,
                               'news_contents':news_contents})
                browser.close()
                pass
                browser.switch_to.window(current_window_handle)

            next_btn.click()

# url 주소 변수 지정


# json 파일을 dictionary 형태로 변환
pass

# mongoDB 저장
