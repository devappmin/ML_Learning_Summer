import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./data/pima-indians-diabetes.csv', names=[
                 'pregnant', 'plasma', 'pressure', 'thickness0', 'ilsulin', 'BMI', 'pedigree', 'age', 'class'])

# 임신 횟수 비만에 영향을 끼칠까
# 비만도 유전인가?
# pregnant, class // groupby

a = df.groupby('pregnant')['class'].mean()

facet = sns.FacetGrid(df, col='class')
facet.map(plt.hist, 'plasma', bins=10,)
plt.show()
