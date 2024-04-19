# 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException    # Element : 웹요소 찾지 못할 때 / Window : 창이 없거나 찾을 수 없을 때
# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
from selenium.webdriver.common.by import By
# - 정보 획득
# from selenium.webdriver.support.ui import Select      # Select : dropdown 메뉴 다루는 클래스
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 몽고db 저장
from pymongo import MongoClient
# mongodb에 접속
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["get_stock"]
# collection 작업
hancoms = database['hancom']
# - 주소 입력
browser.get("https://finance.naver.com/item/sise_day.naver?code=030520&page=1")

time.sleep(2)


# 페이지 네이션 가져오기
page_nation_value = "body > table.Nnavi > tbody"
page_nation_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=page_nation_value)

time.sleep(1)

# 마지막 페이지 진입
click_button_last = browser.find_element(by=By.CSS_SELECTOR,value = 'body > table.Nnavi > tbody > tr > td.pgRR > a').click()
time.sleep(1)

# 페이지 번호 가져오기
number_text = browser.find_element(by=By.CSS_SELECTOR,value = 'body > table.Nnavi > tbody > tr > td.on > a').text
time.sleep(1)

# 특정 날짜에서 멈추기 위한 플래그
flag = False

for i in range(int(number_text)):
    page = i + 1
    browser.get(f"https://finance.naver.com/item/sise_day.naver?code=030520&page={page}")

    time.sleep(1)
    # 주가 정보 영역 가져오기
    
    selector_value = "body > table.type2 > tbody > tr"
    element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)


    for element in element_bundle:

        try:
            date = element.find_element(by=By.CSS_SELECTOR, value=f'td:nth-child(1)> span').text
            # 뉴스를 수집한 기간에 맞춰서 수집 종료
            if date in ['2017.12.31','2017.12.30','2017.12.29','2017.12.28','2017.12.27']:
                flag = True
        except:
            date = None

        try:
            end_price = element.find_element(by=By.CSS_SELECTOR, value=f'td:nth-child(2)> span').text
            end_price = end_price.replace(',','')
            end_price = int(end_price)
            pass
        except:
            end_price = None

        try:
            daily_change = element.find_element(by=By.CSS_SELECTOR, value=f'td:nth-child(3)> span').text
            if daily_change != '0':
                try:
                    updown = element.find_element(by=By.CSS_SELECTOR, value='td:nth-child(3) > img[alt="하락"]')
                    daily_change = '-' + daily_change
                except:
                    updown = element.find_element(by=By.CSS_SELECTOR, value='td:nth-child(3) > img[alt="상승"]')
                    daily_change = '+' + daily_change
        except:
            daily_change = None

        try:
            start_price = element.find_element(by=By.CSS_SELECTOR, value=f'td:nth-child(4)> span').text
            start_price = start_price.replace(',','')
            start_price = int(start_price)
        except:
            start_price = None

        try:
            high_price = element.find_element(by=By.CSS_SELECTOR, value=f'td:nth-child(5)> span').text
            high_price = high_price.replace(',','')
            high_price = int(high_price)
        except:
            high_price = None

        try:
            low_price = element.find_element(by=By.CSS_SELECTOR, value=f'td:nth-child(6)> span').text
            low_price = low_price.replace(',','')
            low_price = int(low_price)
        except:
            low_price = None

        try:
            trade = element.find_element(by=By.CSS_SELECTOR, value=f'td:nth-child(7)> span').text
            trade = trade.replace(',','')
            trade = int(trade)
        except:
            trade = None

        data={
        'date' : date,
        'end_price' : end_price,
        'daily_change' : daily_change,
        'start_price' : start_price,
        'high_price' : high_price,
        'low_price' : low_price,
        'trade' : trade
        }
        hancoms.insert_one(data)
        if flag:
            break
    if flag:
        break




browser.close()
