import seaborn as sns
import matplotlib.pyplot as plt

anscombe = sns.load_dataset('anscombe')

data1 = anscombe[anscombe['dataset'] == 'I']
data2 = anscombe[anscombe['dataset'] == 'II']
data3 = anscombe[anscombe['dataset'] == 'III']
data4 = anscombe[anscombe['dataset'] == 'IV']

# data = [data1, data2, data3, data4]

# for i in data:
#     # 평균
#     print(i.mean())

fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.plot(data1['x'], data1['y'], 'o')
ax2.plot(data1['x'], data1['y'], 'o')
ax3.plot(data1['x'], data1['y'], 'o')
ax4.plot(data1['x'], data1['y'], 'o')

ax1.set_title('Data1')
ax2.set_title('Data2')
ax3.set_title('Data3')
ax4.set_title('Data4')

plt.show()
