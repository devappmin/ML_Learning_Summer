from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
import requests


total = []

for i in range(0, 2):
    url = requests.get(
        'https://finance.naver.com/sise/sise_market_sum.nhn?sosok={}&page=1'.format(i))

    html = BeautifulSoup(url.text, features="html.parser")

    kospi_page = int(
        html.find('td', attrs={'class': 'pgRR'}).find('a')['href'][-2:])
    for n in tqdm(range(1, kospi_page + 1)):
        url = requests.get(
            'https://finance.naver.com/sise/sise_market_sum.nhn?sosok={}&page={}'.format(i, n))
        html = BeautifulSoup(url.text, features="html.parser")
        items = html.find('table', attrs={'class': 'type_2'})

        df = pd.read_html(str(items))[0]
        df = df[df['종목명'].notnull()]
        del df['N']
        del df['토론실']
        df['종류'] = ['KOSPI' if i == 0 else 'KOSDAQ'] * len(df)
        df['페이지'] = [n] * len(df)
        total.append(df)
total = pd.concat(total, ignore_index=True)
total.to_excel('sise.xlsx')
