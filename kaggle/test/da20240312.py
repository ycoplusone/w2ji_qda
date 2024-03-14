'''
분석목표 : 
    - 주어진 각 feature를 통해 생존자/사망자 별로 데이터 분리하여 살펴보기
    - 어떤 정보를 통해 생존율을 예측할수 있을지 , 가설을 세우고 실제 그래프로 검증해봅시다.

알고리즘 : 
종속변수 : survived (생존여부)
평가지표 : 
사용모델 : 
데이터셋 : 891명의 승객에 대한 데이터
survived    / 생존여부          / int64    / [0 1] 
alive       / 생존여부          / object   / ['no' 'yes']
sex         / 성별              / object   / ['male' 'female']
class       / 티켓등급          / category / ['Third', 'First', 'Second']
pclass      / 티켓등급          / int64    / [3 1 2]
deck        / 좌석구역          / category / [NaN, 'C', 'E', 'G', 'D', 'A', 'B', 'F']
who         / 남성,여성,아이    / object    / ['man' 'woman' 'child']
adult_male  / 성인 남자 여부    / bool      / [ True False]
embarked    / 출항지           / object    / ['S' 'C' 'Q' nan]
embark_town / 출항지           / object    / ['Southampton' 'Cherbourg' 'Queenstown' nan]
alone       / 혼자여부         / bool      / [False  True]
age         / 나이             / float64   / [ to many ]
fare        / 요금             / float64   / [ to many ]
sibsp       / 탑승자자녀수      / int64     / [1 0 3 4 2 5 8]
parch       / 탑승자부모수      / int64     / [0 1 2 5 3 4 6]
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 데이터 로드
titanic_df = sns.load_dataset('titanic')
df = titanic_df.drop(columns=['survived']) #종속변수를 제외한 독립변수들만 처리.

# 2. 데이터의 구분을 확인한다.
#for i in df.columns:    
#    print( i ,'/' ,df[i].dtype , '/',  df[i].unique()   )

# 3. 범주형 데이터와 수치형 데이터
category_cols  = ["sex","embarked","class","who","adult_male","deck","embark_town","alive","alone"]
numerical_cols = ["age","sibsp","parch","fare"]

# 4. 데이터의 분포를 데이터 시각화로 확인.
plt.rc('font', family='Malgun Gothic')
figure, ax_list = plt.subplots(nrows=1, ncols= 4 )

for i in range( 4 ):
    col = numerical_cols[i]
    sns.boxplot(data=df, y=col, showfliers=True, ax=ax_list[i] , palette='tab10' )
    ax_list[i].set_title( col )
plt.show()

figure, ax_list_list = plt.subplots(nrows=3, ncols=3);

ax_list = ax_list_list.reshape(9)  # 다차원 행렬의 차원을 원하는 모양으로 변경합니다.
#print(ax_list_list.shape)
#print(ax_list.shape)

for i in range(len(category_cols)):
    col = category_cols[i]
    sns.countplot(data=df, x=col, ax=ax_list[i] , palette='tab10')
    ax_list[i].set_title(col)
plt.tight_layout()
plt.show()

# 성별과 생존 여부
sns.countplot(data=df, x='sex', hue='alive' );
plt.title('성별과 생존 여부')
plt.show()

# 좌석 등급과 생존 여부
sns.countplot(data=titanic_df, x='pclass', hue='alive');
plt.title('좌석 등급과 생존 여부')
plt.show()


# 9개의 범주형 분류에 대해, 생존 여부로 그래프 그리기
figure, ax_list_list = plt.subplots(nrows=3, ncols=3);
figure.set_size_inches(10,10)

ax_list = ax_list_list.reshape(9)
print(ax_list_list.shape)
print(ax_list.shape)

for i in range(len(category_cols)):
    col = category_cols[i]
    sns.countplot(data=titanic_df, x=col, ax=ax_list[i], hue='survived')
    ax_list[i].set_title(col)

plt.tight_layout()
plt.show()
'''
- 남성보다 여성의 생존률이 더 높습니다 (남성 > 여성 > 아이)
- 탑승지(embarked)가 C인 경우 생존율이 높습니다
- 1등석 > 2등석 > 3등석 순으로 생존율이 높습니다
- B,D,E 덱 위치의 승객들이 생존율이 높습니다
- 나홀로 승객은 생존율이 낮습니다
'''
