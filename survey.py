import pandas as pd

site = pd.read_csv('./data/survey_site.csv')
person = pd.read_csv('./data/survey_person.csv')
survey = pd.read_csv('./data/survey_survey.csv')
visited = pd.read_csv('./data/survey_visited.csv')


# 특정 위치의 날씨 정보
# person: 관측한 사람 이름
# site: 관측 위치
# survey: 날씨 정보
# visited: 관측 날짜


total = site.merge(visited, left_on='name', right_on='site')
total = total.merge(survey, left_on='ident', right_on='taken')
total = total.merge(person, left_on='person', right_on='ident')
print(total)
