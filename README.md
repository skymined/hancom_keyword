# 주식과 뉴스의 만남 주스

## 1. 프로젝트 소개

오늘도 킹킹반영을 하지못해 주식에서 돈을 꼴아버린 나는야 개미...
도대체 킹킹반영을 못해서 뉴스가 나오면 이미 다 끝나버린 주식들...
도대체 그 상관관계에는 뭐가 있을까 너무 궁금해졌다.

### 팀원 소개
|이름|담당|비고|
|--|--|--|
|박요한|크롤링, 분석||
|김하늘|크롤링||
|노주현|크롤링||

## 2. 전략
### 변인 통제 설정


### 가정


### 가설



## 3. 데이터 수집

대상 사이트(뉴스) : [다음뉴스](https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=%ED%95%9C%EA%B8%80%EA%B3%BC+%EC%BB%B4%ED%93%A8%ED%84%B0)

대상 사이트(주식정보) : [네이버증권](https://finance.naver.com/item/sise.naver?code=030520)


|담당|기간|코드|
|--|--|--|
|박요한|2022.01 ~ 2023.12|[news](./selenium/yohan/stock_news.py) / [stock](./selenium/yohan/get_stock.py)|
|김하늘|2018.01 ~ 2019.12||
|노주현|2020.01 ~ 2021.12||

## 4. 분석


<img src="./images/stock_line.png" alt="자체제작 그래프" width="400"/> <img src="./images/stock_from_naver.png" alt="네이버 그래프" width="400"/>
```
그래프가 잘 그려졌다.
```
<img src="./images/checkpoint_count.png" alt="체크포인트 카운트" width="400"/> <img src="./images/stock_changed.png" alt="체크포인트 비율" width="400"/>
```
여기는 나중에 수정 체크포인트랑 전일비 음양값은 상관이 없지
```

![체크포인트 하이라이트 그래프](./images/checkpoint_graph.png)
```
붉은 점이 눈여겨볼만한 곳 - 가격과 트레이딩이 모두 외부요인이 작용했다고 여겨지는 날짜
```

우선 뉴스 데이터 전처리? LDA 할 수 있도록 전처리 작업 한번 하고
그 분석에서 뭔가 나왔던 점들의 뉴스 갯수 (일평균 내서 그거보다 많은지 아닌지) 기간은 한 플마 2일정도

유의미한 곳에서 뉴스 LDA 진행하고 분석

오버랩 체크포인트는 따로 모아서 특별히 보여주고

전일비 + - 를 나눠서 거래량 포인트랑 비교해보는것도 괜찮을듯 (거래는 많은데 가격방어가 되었다? 혼조세면 뉴스랑 뭔가 있을거같기도 하고 또다른 외부요인이 있을지도)

결론으로 뉴스 토픽과 상관관계 조금 분석해 보고, 그리고 뭔가... 뭔가 있다...?

## 기타


- <a href="https://docs.google.com/spreadsheets/d/11cNZtdvFaNoGP85uGBtqYcHx3JYqYZZ--ZaGSV2Z_IU/edit?usp=sharing">스케쥴러</a>
