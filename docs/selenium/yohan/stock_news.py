# 여기는 그 주식 뉴스 스크래핑

# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory)
                           , options=chrome_options)



# 몽고db 저장
from pymongo import MongoClient
# mongodb에 접속
# mongoClient = MongoClient("mongodb://192.168.10.10:27017")
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["news_get"]
# collection 작업
news_get = database['daum_news']

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
from selenium.webdriver.common.by import By

# url = 'https://search.daum.net/search?w=news&nil_search=btn&DA=STC&enc=utf8&cluster=y&cluster_page=1&q=%ED%95%9C%EA%B8%80%EA%B3%BC+%EC%BB%B4%ED%93%A8%ED%84%B0&sd=20220101000000&ed=20231231235959&period=u&p=1&sort=old'
# url = 'https://search.daum.net/search?nil_suggest=btn&w=news&DA=STC&cluster=y&q=%ED%95%9C%EA%B8%80%EA%B3%BC+%EC%BB%B4%ED%93%A8%ED%84%B0&sd=20220521000000&ed=20231231235959&period=u&sort=old'
# url = 'https://search.daum.net/search?nil_suggest=btn&w=news&DA=STC&cluster=y&q=%ED%95%9C%EA%B8%80%EA%B3%BC+%EC%BB%B4%ED%93%A8%ED%84%B0&sd=20220925000000&ed=20231231235959&period=u&sort=old'
# url = 'https://search.daum.net/search?nil_suggest=btn&w=news&DA=STC&cluster=y&q=%ED%95%9C%EA%B8%80%EA%B3%BC+%EC%BB%B4%ED%93%A8%ED%84%B0&sd=20230224000000&ed=20231231235959&period=u&sort=old'
# url = 'https://search.daum.net/search?nil_suggest=btn&w=news&DA=STC&cluster=y&q=%ED%95%9C%EA%B8%80%EA%B3%BC+%EC%BB%B4%ED%93%A8%ED%84%B0&sd=20230817000000&ed=20231231235959&period=u&sort=old'
url = 'https://search.daum.net/search?nil_suggest=btn&w=news&DA=STC&cluster=y&q=%ED%95%9C%EA%B8%80%EA%B3%BC+%EC%BB%B4%ED%93%A8%ED%84%B0&sd=20231229000000&ed=20231231235959&period=u&sort=old'

browser.get(url)
time.sleep(2)

element_body = browser.find_element(by=By.CSS_SELECTOR,value='body')

main_window_handle = browser.current_window_handle # 초기 창 핸들로 저장


counter = 0
while True:


    # 뉴스 리스트 저장
    news_list = browser.find_elements(by=By.CSS_SELECTOR,value='#dnsColl > div:nth-child(1) > ul >li')
    
    for news in news_list:
        time.sleep(2)
        # 뉴스 진입
        try:
            click_news = news.find_element(by=By.CSS_SELECTOR,value='#dnsColl > div:nth-child(1) > ul > li > div.c-item-content > div > div.item-title > strong > a').click()
        except:
            break

        # 새창 뉴스
        all_window_handles = browser.window_handles # 모든 창 저장

        # 새 창 핸들을 찾기
        new_window_handle = None
        for handle in all_window_handles:
            if handle != main_window_handle:    #현재 창이 메인창이 아닐때
                new_window_handle = handle  # 현재 창이 새로운창으로 핸들
                break

        # 새 창 핸들로 전환
        browser.switch_to.window(new_window_handle)


        # 새 창의 URL 가져오기
        current_url = browser.current_url
        # 새창 정보 획득
        browser.get(current_url)

        time.sleep(1)

        inside_element_gets = browser.find_elements(by=By.CSS_SELECTOR,value='body') #새창의 엘리맨츠 가져오기
        pass

        for inside_element_get in inside_element_gets:
            
            # 타이틀
            try:
                selector_title = '#mArticle > div.head_view > h3'
                element_title = inside_element_get.find_element(by=By.CSS_SELECTOR,value=selector_title)
                title = element_title.text
            except:
                title = ""

            # 날짜
            try:
                selector_time = "#mArticle > div.head_view > div.info_view > span:nth-child(2) > span"
                element_time = inside_element_get.find_element(by=By.CSS_SELECTOR,value=selector_time)
                times = element_time.text
            except:
                times = ""


            # 내용
            content = ''
            try:
                selector_content_2= "#mArticle > div.news_view.fs_type1 > strong"
                element_content = inside_element_get.find_element(by=By.CSS_SELECTOR,value=selector_content_2)
                content += element_content.text
                content += ' '
            except:
                pass
            try:
                selector_content_1= "#mArticle > div.news_view.fs_type1 > div.article_view"
                element_content = inside_element_get.find_element(by=By.CSS_SELECTOR,value=selector_content_1)
                content += element_content.text
            except:
                pass

            # 언론사
            
            try:
                selector_media = "#mArticle > div.news_view.fs_type1 > p"
                element_media = inside_element_get.find_element(by=By.CSS_SELECTOR,value=selector_media)
                text_list = list(element_media.text.split())
                media = text_list[1][:-1]
            except:
                media = ""

            # mongodb 저장
            data = {
                'news_title' : title,
                'news_date' : times,
                'news_brand' : media,
                'news_contents' : content
            }
            pass
            news_get.insert_one(data)

        time.sleep(2)
        browser.close() # 새로 열린창 닫기
        browser.switch_to.window(main_window_handle)    # 다시 처음 창으로 전환

    # 다음 페이지 클릭
    try:
        element_click = browser.find_element(by=By.CSS_SELECTOR,value=f'#dnsColl > div:nth-child(2) > div > button.btn_next')
        element_click.click()
        time.sleep(2)
    except:
        break

        
        
    time.sleep(2)

# 브라우저 종료
browser.quit()