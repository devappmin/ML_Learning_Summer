import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('https://bit.ly/perch_csv')

perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
                         115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
                         150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
                         218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
                         556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
                         850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
                         1000.0])

perch_full = df


train_input, test_input, train_target, test_target = train_test_split(
    perch_full, perch_weight)

# 요인 늘리는 방법
# poly = PolynomialFeatures()  # 모델 생성
# poly.fit([[2, 3]])  # 모델 학습
# ans = poly.transform([[2, 3]])  # 변환
poly = PolynomialFeatures()  # 모델 생성
poly.fit(train_input)  # 모델 학습
train_poly = poly.transform(train_input)  # 변환
test_poly = poly.transform(test_input)
# print(poly.get_feature_names())

lr = LinearRegression()
lr.fit(train_poly, train_target)

print(lr.score(train_poly, train_target))
print(lr.score(test_poly, test_target))

poly = PolynomialFeatures(degree=5)  # 5제곱까지 허용
poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

lr = LinearRegression()
lr.fit(train_poly, train_target)
print(train_poly.shape)
print(lr.score(train_poly, train_target))
print(lr.score(test_poly, test_target))


ss = StandardScaler()
ss.fit(train_poly)

train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)

lr = LinearRegression()
lr.fit(train_scaled, train_target)
print(train_poly.shape)
print(lr.score(train_scaled, train_target))
print(lr.score(test_scaled, test_target))
