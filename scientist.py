import pandas as pd

scientiests = pd.read_csv("./data/scientists.csv")


born_dt = pd.to_datetime(scientiests['Born'], format='%Y-%m-%d')
died_dt = pd.to_datetime(scientiests['Died'], format='%Y-%m-%d')

scientiests['Born'] = born_dt
scientiests['Died'] = died_dt

scientiests['Days'] = scientiests['Died'] - scientiests['Born']
# print(scientiests)

# scientiests.to_excel('life_of_scientiests.xlsx')
# scientiests.to_csv('life_of_scientiests.csv')

# 데이터 저장 방법

# 시리즈 저장방법
age = scientiests['Age']
age.to_pickle('age.pickle')

# read_age = pd.read_pickle('age.pickle')
# print(read_age)

scientiests.to_pickle('scientiests.pickle')
read_scientiests = pd.read_pickle('scientiests.pickle')
print(read_scientiests)
