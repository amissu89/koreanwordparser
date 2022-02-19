from importlib.resources import path
import pandas as pd
import os

current_dir = os.getcwd()
path_dir = current_dir + '/dictionary'
file_list = os.listdir(path_dir)

rmColList = [
    
    '구성 단위', '원어·어종', '원어', '어원',
    '발음', '활용', '검색용 이형태', 
    '의미 번호', '방언 지역', '문형', '문법', '용례', 
    '전문 분야', '속담', '관용구', '대역어', '생물 분류군 정보',
    '역사 정보',  '수어 정보', '규범 정보', '다중 매체(멀티미디어) 정보'
]

## 뜻풀이 : 규범 표기, 준말, 피동사, 사동사, 높임말 이 포함되어 있으면 삭제
rmMeaningList = ['규범 표기', '준말', '피동사', '사동사',
                '높임말', '방언', '느낌을 준다']
# join함수를 이용하여 이어주고 contains 함수에 넣기
rmMeaning = '|'.join(rmMeaningList)

rmColList2 = ['고유어 여부', '범주']

for filename in file_list:
    sn = 'Sheet0'

    xls = path_dir + "/" + filename
    print(filename)
    df = pd.read_excel(xls, sheet_name=sn)
    df = df.drop(rmColList, axis=1)

    #"범주"에서 방언, 북한어, 옛말 삭제. 아니면 공백인것만 남기기
    #"고유어 여부"에서 혼종어 삭제
    verb = df[df.품사 == '동사']
    verb = verb[verb['고유어 여부'] == '고유어']
    verb = verb[verb['범주'].isnull()]
    verb = verb[~verb['뜻풀이'].str.contains(rmMeaning)]
    verb = verb.drop(rmColList2, axis=1)
    verb = verb.drop_duplicates('어휘')
    toFile = "g_verb.csv"
    verb.to_csv(toFile, encoding='utf-8', mode='a')

    adj  = df[df.품사 == '형용사'] 
    adj = adj[adj['고유어 여부'] == '고유어']
    adj = adj[adj['범주'].isnull()]
    adj = adj[~adj['뜻풀이'].str.contains(rmMeaning)]
    adj = adj.drop(rmColList2, axis=1)
    adj = adj.drop_duplicates('어휘')
    toFile = "g_adj.csv"
    adj.to_csv(toFile, encoding='utf-8', mode='a')

