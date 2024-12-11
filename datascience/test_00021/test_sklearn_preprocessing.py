'''
sklearn 패키지의 preprocessing 서브패키지도 스케일및 변수변환을 위한 standarscaler 클래스를 제공한다.
1. 학습용 데이터ㅡㄹ 입력으로 fit() 메서드를 실행하면 평균값과 표준편차를 계산하여 객체내에 저장한다.
2. 다시 학습용 데이터를 입력으로 하여 transform() 메서드를 실행하면 
    저장했던 평균값을 빼서 새로운 평균값이 0이되도록 만들고, 
    저장한 표준편차를 나누어 새로운 표준편차가 1이 되도록 데이터를 변환하여 출력한다.
    1단계와 2단계를 합쳐서 fit_transform() 메서드를 실행할수 있다.
3. 검증용 데이터를 입력하여 transform() 메서드를 실행해서
    학습용 데이터의 평균값과 표준편차를 사용하여 검증용 데이터를 변환한다.
'''
import numpy as np
from sklearn.preprocessing import StandardScaler

x = np.arange(7).reshape(-1,1)
print(x)

scaler = StandardScaler()
scaler.fit_transform(x)
