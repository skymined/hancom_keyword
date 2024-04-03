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
dabangs = database['hancom']
# - 주소 입력
browser.get("https://finance.naver.com/item/sise_day.naver?code=030520&page=1")

time.sleep(2)


# 페이지 네이션 가져오기
page_nation_value = "body > table.Nnavi > tbody"
page_nation_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=page_nation_value)

counter = 0
while True:
    counter += 1
    if counter != 1:
        
        pass


    break


# 주가 정보 영역 가져오기
selector_value = "#body > table.type2 > tbody"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)




for i in range(24):
    # url = browser.current_url
    # browser.get(url)
    time.sleep(2)
    button_list = browser.find_elements(by=By.CSS_SELECTOR,value = '#content > div.styled__Content-sc-1nnkzie-0.fTqXoR > div.styled__ListWrap-sc-5dgg47-0.fOZpfA > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div')
    for button in button_list:
        click_button_next = button.find_element(by=By.CSS_SELECTOR,value = 'button:nth-child(8)')
    

    ## 전체 방 영역 정보
    room_value = "#content > div.styled__Content-sc-1nnkzie-0.fTqXoR > div.styled__ListWrap-sc-5dgg47-0.fOZpfA > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > ul>li"
    element_whole = browser.find_elements(by=By.CSS_SELECTOR, value=room_value)
    # 상품 클릭(click)
    counter = 0
    for room_element in element_whole:
        counter += 1
        click_item = room_element.find_element(by=By.CSS_SELECTOR, value= f"#content > div.styled__Content-sc-1nnkzie-0.fTqXoR > div.styled__ListWrap-sc-5dgg47-0.fOZpfA > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > ul > li:nth-child({counter}) > div")
        click_item.click()
        time.sleep(2)

        pass
        ## 매물번호 영역
        element_rental_info = browser.find_elements(by=By.CSS_SELECTOR,value = "#content > div.styled__DetailContainer-sc-1xo573q-0.eTmfeO > div > aside > div > div.styled__InfoWrap-sc-1h4thfr-0.cWFdmE")
        for element in element_rental_info:
            # 상품 제목(매물번호-title)
            try:
                element_title = element.find_element(by=By.CSS_SELECTOR,value = "div > div > div.styled__TagWrap-sc-1h4thfr-2.gWqFHA > div > div").text
            except NoSuchElementException:
                element_title = ""
            # 평수(py)
            try:
                element_py = element.find_element(by=By.CSS_SELECTOR,value = "ul > li:nth-child(1) > div:nth-child(2) > span").text
            except NoSuchElementException:
                element_py = ""
            # 지역(region)
            try:
                element_region = element.find_element(by=By.CSS_SELECTOR,value = "ul > li.styled__SubInfo-sc-1h4thfr-14.btBOxM > div:nth-child(2) > p.content").text
            except NoSuchElementException:
                element_region = ""
        ## 가격 정보 영역
        element_price_info = browser.find_elements(by=By.CSS_SELECTOR,value = "div > div.styled__InfoContainer-sc-1xo573q-1.hKVCpS > section:nth-child(1)")
        for element in element_price_info:
            # 보증금,월세가격(depositAndRentFee)
            try:
                element_deposit = element.find_element(by=By.CSS_SELECTOR,value = "#content > div.styled__DetailContainer-sc-1xo573q-0.eTmfeO > div > div > div.styled__InfoContainer-sc-1xo573q-1.hKVCpS > section:nth-child(1) > ul > li:nth-child(1) > div.styled__ListContent-mttebe-1.bQSaMO > p").text
                deposit,rentFee = element_deposit.split('/') # 보증금/월세 split
                deposit += '만원'
                rentFee += '만원'
                pass
            except NoSuchElementException:
                deposit,rentFee = "",""
        ## 상세정보 영역
        element_detail_info = browser.find_elements(by=By.CSS_SELECTOR,value = "div > div.styled__InfoContainer-sc-1xo573q-1.hKVCpS > section:nth-child(2)")
        for element in element_detail_info:
            # 1인실 or 그 외(roomType) - 방 수 1개면 1인실, 2개면 '그 외'
                ## (방 수/욕실 수) -> split 필요?
            try:
                element_roomType = element.find_element(by=By.CSS_SELECTOR,value = "li:nth-child(4) > div.styled__ListContent-ialnoa-7.iMduqg > p").text
                roomtype_list = list(element_roomType.split('/'))
                roomType = roomtype_list[0]
                if roomType == '1개':
                    roomType = '1인실'
                else:
                    roomType = '그 외'
                pass
            except NoSuchElementException:
                roomType = ""
        ## 옵션,보안/안전시설 영역
        element_option_one = browser.find_elements(by=By.CSS_SELECTOR,value = "div > div.styled__InfoContainer-sc-1xo573q-1.hKVCpS > section:nth-child(3)")
        element_option_two = browser.find_elements(by=By.CSS_SELECTOR,value = "div > div.styled__InfoContainer-sc-1xo573q-1.hKVCpS > section:nth-child(4)")
        # 옵션(roomOption)
        for element in element_option_one:
            try:
                element_roomOption_one = element.find_element(by=By.CSS_SELECTOR, value = 'div > div > div.styled__InfoContainer-sc-1xo573q-1.hKVCpS > section:nth-child(3) > ul').text
                pass
            except NoSuchElementException:
                element_roomOption_one = ""
                pass
        # 보안/안전시설
        for element in element_option_two:
            try:
                element_roomOption_two = element.find_element(by=By.CSS_SELECTOR, value = 'div > div > div.styled__InfoContainer-sc-1xo573q-1.hKVCpS > section:nth-child(4) > ul').text
            except NoSuchElementException:
                element_roomOption_two = ""
            pass
        element_roomOption_total = element_roomOption_one +'\n'+ element_roomOption_two
        # 출력값 : '벽걸이형\n침대\n신발장\n냉장고\n세탁기\n싱크대\n가스레인지\nTV\n벽걸이형\n침대\n신발장\n냉장고\n세탁기\n싱크대\n가스레인지\nTV'
        gender = '공용'
        brandType = '일반사업자'
        imgUrl = 'https://d1774jszgerdmk.cloudfront.net/1024/uCtHEMbF1I79lfPgIhws5'
        data={
            'title' : element_title,
            'roomName' : element_title,
            'gender' : gender,
            'roomType' : roomType,
            'py' : element_py,
            'deposit' : deposit,
            'rentFee' : rentFee,
            'region' : element_region,
            'brandType' : brandType,
            'roomOption' : element_roomOption_total,
            'url' : url,
            'imgUrl' : imgUrl
        }
        dabangs.insert_one(data)
        browser.close()
        time.sleep(1)
    time.sleep(5)
    click_button_next.click()  # 페이지 넘기기(2~24페이지)
    

    pass