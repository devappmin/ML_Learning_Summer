import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 도미 데이터
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

# 빙어 데이터
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3,
                11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7,
                10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]


# 머신 러닝
# 문제 : 2차원 배열(리스트)
# 정답 : 1차원 배열

fish_data = []
length = bream_length + smelt_length
weight = bream_weight + smelt_weight

fish_target = [1] * 35 + [0] * 14

for i, j in zip(length, weight):
    fish_data.append([i, j])

kn = KNeighborsClassifier()  # 모델 생성
kn.fit(fish_data, fish_target)  # 학습

# print(kn.score(fish_data, fish_target))  # 평가

# 예측
# print(kn.predict([[30, 600]]))

# 무엇을 통해서 학습을 했는지 알 수 있다.
# print(kn._fit_X)

# 어떤 정답을 가졌는지 알 수 있다
# print(kn._y)

# 생선 49개 // 새로운 데이터가 들어왔을 때 가장 가까운 것 49개를 잡고 다수결
# kn49 = KNeighborsClassifier(n_neighbors=49)
# kn49.fit(fish_data, fish_target)
# print(kn49.score(fish_data, fish_target))

# for n in range(1, 50):
#     kn.n_neighbors = n
#     score = kn.score(fish_data, fish_target)
#     print(n, score)

# 훈련 세트와 테스트 세트 나누기
# train_input = fish_data[:35]
# train_target = fish_target[:35]

# test_input = fish_data[35:]
# test_target = fish_target[35:]

# kn = KNeighborsClassifier()
# kn.fit(train_input, train_target)
# print(kn.score(test_input, test_target))


input_arr = np.array(fish_data)
target_arr = np.array(fish_target)
# print(input_arr)
# print(target_arr)

index = np.arange(49)
np.random.shuffle(index)
print(index)

train_input = input_arr[index[:35]]
train_target = input_arr[index[:35]]

test_input = input_arr[index[35:]]
test_target = input_arr[index[35:]]

plt.scatter(train_input[:, 0], train_input[:, 1])
plt.scatter(test_input[:, 0], test_input[:, 1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
# 출력
# plt.scatter(bream_length, bream_weight)
# plt.scatter(smelt_length, smelt_weight)
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()
