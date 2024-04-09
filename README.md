# 주식과 뉴스의 만남 주스

## 1. 프로젝트 소개

오늘도 킹킹반영을 하지못해 주식에서 돈을 꼴아버린 나는야 개미...
도대체 킹킹반영을 못해서 뉴스가 나오면 이미 다 끝나버린 주식들...
도대체 그 상관관계에는 뭐가 있을까 너무 궁금해졌다.

### 팀원 소개
|이름|담당|비고|
|--|--|--|
|박요한|크롤링, 분석, 스케쥴링, 기획|kdtyohan@gmail.com|
|김하늘|크롤링|adsky0309@gmail.com|
|노주현|크롤링|njh2720@gmail.com|

## 2. 목표
### 가정
- 마케팅 뉴스는 주가에 영향을 줄 것이다.
### 분석대상
- 주가에 영향이 있었던 날의 뉴스들에 대한 토픽을 분석
    + 토픽에 따라 마케팅에 효율적으로 사용할 수 있는 요소들이 무엇인지 알아보자

## 3. 데이터 수집

대상 사이트(뉴스) : [다음뉴스](https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=%ED%95%9C%EA%B8%80%EA%B3%BC+%EC%BB%B4%ED%93%A8%ED%84%B0)

대상 사이트(주식정보) : [네이버증권](https://finance.naver.com/item/sise.naver?code=030520)


|담당|기간|코드|
|--|--|--|
|박요한|2022.01 ~ 2023.12|[news](./selenium/yohan/stock_news.py) / [stock](./selenium/yohan/get_stock.py)|
|김하늘|2018.01 ~ 2019.12||
|노주현|2020.01 ~ 2021.12||

## 4. 분석
|내용|산출물|코드|
|--|--|--|
|뉴스 전처리|[뉴스 카운팅.pkl](./analysis/yohan/pickles/check_count.pkl) / [뉴스 데이터.pkl](./analysis/yohan/pickles/news_data.pkl)|[ipynb](./analysis/yohan/news_analysis.ipynb)|
|주가정보 전처리|[주가 데이터.pkl](./analysis/yohan/pickles/stock_data.pkl) / [체크포인트 날짜.pkl](./analysis/yohan/pickles/date_dataframe.pkl)|[ipynb](./analysis/yohan/sotck_analysis.ipynb)|
|토픽 분석||[ipynb](./analysis/yohan/total_analysis.ipynb)|


<img src="./images/stock_line.png" alt="자체제작 그래프" width="400"/> <img src="./images/stock_from_naver.png" alt="네이버 그래프" width="400"/>
```
네이버 주식 그래프와 비교했을 때, 큰 오류는 보이지 않는다.
```
<img src="./images/checkpoint_count.png" alt="체크포인트 카운트" width="400"/> <img src="./images/stock_changed.png" alt="체크포인트 비율" width="400"/>
```
[그래프 1] Checkpoint Count Plot
거래량의 변화가 많은 날보다 가격의 변화가 많은 날이 적다.
-> 실제로 거래가 많이 일어나도 가격의 변화에 크게 작용하지 않는다

[그래프 2] Stock Changed on hancom
전일비 가격이 같거나 줄어든 날이 높아졌던 날보다 더 많은 것을 확인
현재 주식가는 확인한 날짜보다 높은 상태
-> 하락 시 가격방어가 잘 되었다 or 상승시 큰폭으로 상승하였다.


해석 : 거래가 많이 일어난 날이 많았으므로, 하락시에도 많은 거래를 통해 가격방어가 잘 이뤄졌었을 것이라고 예상할 수 있다.
```

![체크포인트 하이라이트 그래프](./images/checkpoint_graph.png)
```
붉은 점이 눈여겨볼만한 곳 - 가격과 트레이딩이 모두 외부요인이 작용했다고 여겨지는 날짜
```

![체크포인트 뉴스 카운트 그래프](./images/check_count.png)
```
체크 포인트별 뉴스 갯수 확인 결과 310일 중 9일을 제외하고 해당 날짜에 뉴스가 존재하는것을 확인
하이라이트는 긍정적인 결과(전일비 양값)가 일어난 곳을 표시

그래프를 확인한 결과, 뉴스의 갯수가 적었을 때에도 긍정적인 결과가 발생한 날이 매우 많았음
-> 해당 일의 전날의 영향을 이어받았을 수도 있음
```

## 토픽 추출
- 기사의 갯수가 5개 이하라면 해당 기사가 매우 크게 작용했다고 가정
- 전날의 기사에 영향을 받을 수도 있으므로 5개 미만 기사 중 이전날 기사가 5개 이상인 날짜들은 제외
- 결과, 총 3일만 유효한 날이라고 확인하였음

- 토픽 분석 결과

|날짜|기사 수|분석 결과|
|--|--|--|
|2020-09-03|2|52주 신고가 달성 기사만 있는 것으로 보아 테마주 or 마케팅이 아닌 다른 외부요인(실적 발표 등)이 작용한 것으로 판단|
|2022-01-28|1|기사 내 한컴라이프케어(6개월 연장, 8월 예정) 즉, 락업이 연장되는 것이 주요 작용을 한것으로 예상|
|2022-02-15|4|싸이월드에 관련된 기사가 많음, 해당 시기 메타버스 및 NFT의 주요 투자 시기였다는 것을 감안하면 메타버스 테마주로써 작용한 것으로 판단|


## 기타


- <a href="https://docs.google.com/spreadsheets/d/11cNZtdvFaNoGP85uGBtqYcHx3JYqYZZ--ZaGSV2Z_IU/edit?usp=sharing">스케쥴러</a>
