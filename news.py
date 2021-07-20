import requests
import pandas as pd
import re
from tqdm import tqdm
from bs4 import BeautifulSoup

data = []

dic = {}

textList = ""

for i in tqdm(range(0, 4000, 10)):
    url = requests.get(
        'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%88%AD%EC%8B%A4%EB%8C%80&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=87&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={}'.format(i))

    html = BeautifulSoup(url.text, features="html.parser")

    page = html.find('ul', attrs={'class': 'list_news'}).find_all(
        'li', attrs={'class': 'bx'})

    for i in page:
        title = i.find('a', attrs={'class': 'news_tit'})['title']
        description = i.find('a', attrs={'class': 'api_txt_lines'})
        data.append([title, description.text])
        textList += description.text

# exel = pd.DataFrame(data, columns=['제목', '설명'])
# exel.to_excel('soongsil_news.xlsx')


for i in re.findall('[가-힣]+', textList):
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

dic.sort
print(dic)
