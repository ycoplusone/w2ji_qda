'''
1. autoimpute tutorial
    url : https://kearnz.github.io/autoimpute-tutorials/
'''

# imports
import numpy as np
import pandas as pd
from scipy.stats import norm, binom
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import klib

# seed to follow along
np.random.seed(654654)

# generate 1500 data points
N = np.arange(1500)

# helper function for this data
vary = lambda v: np.random.choice(np.arange(v))

# create correlated, random variables
a = 2
b = 1/2
eps = np.array([norm(0, vary(50)).rvs() for n in N])
y = (a + b*N + eps) / 100                         
x = (N + norm(10, vary(250)).rvs(len(N))) / 100
 
# 20% missing in x, 30% missing in y
x[binom(1, 0.2).rvs(len(N)) == 1] = np.nan
y[binom(1, 0.3).rvs(len(N)) == 1] = np.nan

# collect results in a dataframe 
data_miss = pd.DataFrame({"y": y, "x": x})
sns.scatterplot(x="x", y="y", data=data_miss)

klib.dist_plot( data_miss.x ) # 정규분포를 확인.
#plt.show()

from sklearn.linear_model import LinearRegression

# prep for regression
X = data_miss.x.values.reshape(-1, 1) # reshape because one feature only
y = data_miss.y
lm = LinearRegression()

'''
print(data_miss.head(10))
from autoimpute.imputations import SingleImputer
#data_imputed_once = SingleImputer().fit_transform(data_miss)
#print('data_imputed_once',data_imputed_once)
imputer = SingleImputer(strategy="mean")
data_imputed = imputer.fit_transform(data_miss)
print( data_imputed.head(10) )
'''
df = pd.read_csv('D:\\python_workspace\\w2ji_qda\\kaggle\\guide\\data\\titanic\\train.csv')
df = df[['Age','Sex','Embarked']]


from autoimpute.imputations import SingleImputer, MultipleImputer, MiceImputer
si = SingleImputer() # pass through data once
mi = MultipleImputer() # pass through data multiple times
mice = MiceImputer() # pass through data multiple times and iteratively optimize imputations in each column

mice.fit_transform(df[['Age','Fare']])