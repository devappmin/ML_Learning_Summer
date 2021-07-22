import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='./chromedriver',
                          options=webdriver.ChromeOptions())
driver.get('https://shopping.naver.com/fresh/directfarm/home')

last = driver.execute_script('return document.body.scrollHeight')
total = []

while True:
    source = driver.page_source

    html = BeautifulSoup(source)

    products = html.find_all('li', attrs={'class': '_10KV3Ufxul'})

    for i in products:
        price = i.find('span', attrs={'class': '_3MzrqSUlwR'}).text
        title = i.find('strong', attrs={'class': '_1lxNNH5gfD'}).text
        # if [price, title] not in total:
        #     total.append([price, title])
        total.append([price, title])

    print(f'{len(total)}개 상품 데이터 저장 완료')

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    time.sleep(5)
    new = driver.execute_script('return document.body.scrollHeight;')
    if last == new:
        break
    last = new
