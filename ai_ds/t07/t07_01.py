'''
7장 회귀분석(regression analysis)
#import sklearn as sk #  사이킷럿 모듈
#import statsmodels as sm #전통전인 회귀분석모형 라이브러리
'''

def test1():
    '''statsmodels 예제'''
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import statsmodels.api as sm
    import statsmodels.formula.api as smf    

    nsample = 200
    x1 = np.random.normal(size=nsample , loc=0 , scale=1)
    x2 = np.random.normal(size=nsample , loc=0 , scale=1)
    x3 = np.random.normal(size=nsample , loc=0 , scale=1)

    beta = np.array([1,0.1,10])
    e= np.random.normal(size = nsample)
    y = 3+x1 + 0.1*x2+5*x3+e

    df = pd.DataFrame({'x1':x1, 'x2':x2, 'x3':x3, 'y':y})
    print( df.head() )

    # statsmodels.api.OLS 적용 및 결과
    x = df.loc[:,['x1','x2']]
    x = sm.add_constant(x)
    m0 = sm.OLS(y,x)
    fit0 = m0.fit()
    print(fit0.summary())
    print('*'*50)
    # statsmodels.formula.api.ols 적용 및 결과
    m1 = smf.ols(formula='y ~ x1+x2+x3' , data=df)
    fit1 = m1.fit()
    print( fit1.summary() )

def test2():
    '''sklearn 예제'''
    import numpy as np
    from sklearn import datasets
    from sklearn.model_selection import train_test_split # 데이터분할
    from sklearn.linear_model import LinearRegression    # 선형회귀모형
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler    
    import pandas as pd

    # - 데이터 준비, 훈련/검증데이터로 분할, 데이터 표준화 (필요시)
    x , y = datasets.load_diabetes(return_X_y=True) #데이터 로드
    x_tr , x_te , y_tr , y_te = train_test_split(x,y,test_size=0.3 , random_state=1) # train과 test 분리

    # 데이터 표준화
    scaler = StandardScaler().fit(x_tr)
    x_tr_s = scaler.transform(x_tr)
    x_te_s = scaler.transform(x_te)

    # 회귀모형 적합
    lm = LinearRegression() # linear regression model
    lm.fit(x_tr , y_tr) # 훈련자료로 모형적합(회귀계수 추정)

    # 추정된 회귀계수 출력
    print('beta_0 = ', lm.intercept_)
    print('[beta_1, ..., beta_p] = ', lm.coef_)

    # 검증데이터에 대한 예측
    pred = lm.predict(x_te_s)
    out = pd.DataFrame({'y':y_te , 'y_pred':pred , 'resid': y_te-pred})
    print( out )


    


    

    

test2()






