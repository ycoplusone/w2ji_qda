from patsy import demo_data , dmatrix
import pandas as pd
import numpy as np

# 판다스 데이터 생성.
df = pd.DataFrame( demo_data("x1", "x2", "x3", "x4", "x5") )
print(df)

# df 데이터 프레임의 1개 열만 추출
print( dmatrix("x1 + 0" , data=df) )

# df 데이터 프레임의 다중열 추출
print( dmatrix("x1 + x2 + x3 + 0" , data=df) )

print('*'*20)
# df 데이터 프레임의 함수와도 연결한다.
def fn_test(x):
    # 테스트 함수
    return 10*x
#print( dmatrix("x1 + np.log(np.abs(x2))" , data=df) ) # 다른 라이브러리 연산 
#print( dmatrix("x1 + fn_test(x2)" , data=df) ) # 로컬 함수 연산
#print( dmatrix("x1 + x2 + x1:x2 +0 " , data=df) ) #상호작용
print( dmatrix("x1 + x2 + I(x1+x2) +0 " , data=df) ) # 상호작용없이 바로 연산

print('*'*20)
# 선형회귀분석을 할때 조건수의 영향때문에 데이터의 평균을 0 으로 표준편차를 1로 만드는 스케일링 작업을한다.
# patsy 패키지는 스케일링 함수를 제공한다. 
# center() : 평균을 0으로 스케일링
# standardize() : 평균을 0으로 하고 표준편차를 1로 스케일
# scale() : standardize()와 같음
dm = dmatrix("center(x1) + 0" , data=df)
print( dm ) # 평균을 0으로 스케일
print( df.x1 - np.mean(df.x1) ) # center 함수을 보여준다.
print( dm.design_info.factor_infos ) # 어떻게 생성되어 있는지 알수 있다.