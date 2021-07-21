import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset('tips')
print(tips)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# # 막대그래프
# ax1.hist(tips['total_bill'], bins=10)
# ax1.set_title('Histogram')
# ax1.set_xlabel('Total Bill')
# ax1.set_ylabel('Frequency')


def recode_sex(sex):
    if sex == 'Female':
        return 0
    else:
        return 1


tips['sex_color'] = tips['sex'].apply(recode_sex)

ax1.scatter(x=tips['total_bill'], y=tips['tip'],
            s=tips['tip'] * 10, c=tips['sex_color'], alpha=0.5)

plt.show()
