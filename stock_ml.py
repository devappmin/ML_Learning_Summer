from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests

total = []


driver = webdriver.Chrome(executable_path='./chromedriver',
                          options=webdriver.ChromeOptions())
for n in range(1, 534):
    driver.get(
        f'https://finance.naver.com/item/sise_day.nhn?code=035720&page={n}')
    driver.implicitly_wait(10)
    source = driver.page_source
    html = BeautifulSoup(source)

    table = html.find('table', attrs={'class': 'type2'})
    table = pd.read_html(str(table))[0]
    table = table.dropna()
    total.append(table)

total = pd.concat(total, ignore_index=True)

print(total)
