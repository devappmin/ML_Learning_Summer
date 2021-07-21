from numpy import NaN, NAN, nan
import pandas as pd

ebola = pd.read_csv('./data/country_timeseries.csv')

# ebola = ebola.fillna(0) # NaN을 0으로 채워줌
# ebola = ebola.fillna(method='ffill') # Front Fill
# ebola = ebola.fillna(method='bfill') # Back Fill

# ebola = ebola.interpolate()  # 자기 앞과 자기 뒤의 값을 가져와 나눠준다.

# 평균값
ebola['Cases_Guinea'] = ebola['Cases_Guinea'].fillna(
    ebola['Cases_Guinea'].mean())

print(ebola)
print(ebola['Cases_Guinea'].sum())
