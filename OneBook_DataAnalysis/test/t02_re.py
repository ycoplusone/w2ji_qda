import re

# 태그 추출 함수 정의 ver1
def extract_tag_v1(txt):
    txt = txt.strip();
    return re.findall('#[A-Za-z가-힣]+',str(txt))

def extract_tag_v2(txt):
    txt = txt.strip()
    return re.findall('#\w+',str(txt))

tt ='''메타 문자란 무엇일까요? 메타 문자는 정규표현식내에서 특별한
의미를 갖는 문자를 말합니다. What is the Meta Character?
A metacharacter is a character that has a special meaning to a computer program, 
such as a shell interpreter or a regular expression(regex) engine.
확장 정규식에 쓸수 있는 메타 문자는 *+?$^^.()|\{}[] 등이 있습니다.
#정규식 #정규표현식 #메타문자 #regex #metacharacter
'''
print( extract_tag_v1(tt))
print('-'*50)
print( extract_tag_v2(tt))