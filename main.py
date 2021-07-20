import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm


url = requests.get(
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%A1%9C%EB%98%90%EB%B2%88%ED%98%B8")
html = BeautifulSoup(url.text, features="html.parser")

current = int(
    html.find('a', attrs={'class': '_lotto-btn-current'}).find('em').text[:-1])


total = []

for n in tqdm(range(1, current + 1)):
    url = requests.get(
        'https://search.naver.com/search.naver?ie=UTF-8&query=%EB%A1%9C%EB%98%90%EB%B2%88%ED%98%B8+{}%ED%9A%8C&sm=chr_hty'.format(n))
    html = BeautifulSoup(url.text, features="html.parser")

    box = [n]

    numbers = html.find('div', attrs={'class': 'num_box'}).find_all('span')
    for i in numbers:
        if i.text != '보너스번호':
            box.append(int(i.text))

    total.append(box)

df = pd.DataFrame(
    total, columns=['회차', '1번째번호', '2번째번호', '3번째번호', '4번째번호', '5번째번호', '6번째번호', '보너스 번호'])
df.to_excel('result.xlsx')
