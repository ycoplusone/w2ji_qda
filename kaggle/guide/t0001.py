''' 타이타닉 생존자 예측하기
데이터 특징들(Feature)
    'survived'      => 생존여부 0 : no , 1 :yes
    'pclass'        => 티켓 등급    1 : 1st , 2 : 2nd , 3 : 3rd
    'sex'           => 성별
    'age'           => 나이
    'alone'         => 혼자 여부
    'sibsp'         => 형제 자매 등승 탑승 수
    'parch'         => 자녀 등승 탑승 수
    'fare'          => 요금
    'embark_town'   =>
    'embarked'      => 탑승 항구
    'class'         => 
    'who'           =>
    'adult_male'    =>
    'deck'          =>    
    'alive'         =>
    
'''
import seaborn as sb

data = sb.load_dataset('titanic')

# 1. Feature Engineering 
# - 데이터 클렌징 => 데이터 청소하기 이상치혹은 결측치를 제거하거나 대체하는 행위


