# 셀레니움
# 엑셀파일생성
# 연도별 csv파일
# 2020 2021
# rank 1~50
# 순위정보 / 제목 / 가수 / 좋아요 수

# 2020~2021
# 1위~5위 사이의 가장 많이 max 순위권에 포함된 가수
# 가수별 순위 1~50위 사이 몇번 등록되었는지
# 1~50위 사이 가장 많이 노출된 가수 10명을 대상으로 bar
# 1~50위 랭킹에 노출된 전체 가수의 좋아요 수 평균
# merge 3개년 통합 엑셀 csv파일 1개 생성
# input 사용자입력 통해서 특정 년의 특정 순위 검색 기능/가수 검색 기능 구현
# ex) 검색 년 입력 : 2020 -> 순위 검색 or 가수 검색 : 순위 ->
# 순위 입력 : 38 -> result : 가수명

from selenium import webdriver
import time as t
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def makeString(obj,num):
    listx=[]
    for i in range(num):
        listx.append(obj[i].text)
    return listx

def makeInt(obj,num):
    listx=[]
    for i in range(num):
        listx.append(int(obj[i].text.replace(',','')))
    return listx
chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
url = 'https://www.melon.com/index.htm'
browser.get(url)
# 멜론차트 클릭
browser.find_element(By.XPATH,'/html/body/div/div[2]/div/div[2]/ul[1]/li[1]/a/span[2]').click()
t.sleep(1)
# 시대 클릭
browser.find_element(By.XPATH,'//*[@id="gnb_menu"]/ul[1]/li[1]/div/ul/li[5]/a/span').click()
t.sleep(2)
# 국내 클릭
browser.find_element(By.XPATH,'//*[@id="conts"]/div[2]/ul/li[1]/a/span').click()
t.sleep(2)
# 시대 카테고리 클릭
browser.find_element(By.XPATH,'//*[@id="conts"]/div[3]/div[1]/div/span/span').click()
t.sleep(1)
# 2020년대 클릭
browser.find_element(By.XPATH,'//*[@id="conts"]/div[3]/div[1]/div/div/ul/li[7]/a').click()
t.sleep(1)
# 세부 카테고리 클릭
browser.find_element(By.XPATH,'//*[@id="conts"]/div[3]/div[2]/div/span/span').click()
t.sleep(1)
# 2020년 클릭
browser.find_element(By.XPATH,'//*[@id="conts"]/div[3]/div[2]/div/div/ul/li[2]/a').click()
t.sleep(2)

target_2020_title=browser.find_elements(By.CLASS_NAME,'rank01')
target_2020_name=browser.find_elements(By.CLASS_NAME,'rank02')
target_2020_like=browser.find_elements(By.CLASS_NAME,'cnt')

dict1={'rank2020':range(1,51),
       'title':makeString(target_2020_title,50),
       'name':makeString(target_2020_name,50),
       'like':makeInt(target_2020_like,50)}
col1=['rank2020','title','name','like']
df1=pd.DataFrame(dict1,columns=col1,index=range(50))

df1.to_csv("2020차트.csv",mode='w', index=False, encoding='utf-8-sig')

# 세부 카테고리 클릭
browser.find_element(By.XPATH,'//*[@id="conts"]/div[3]/div[2]/div/span/span').click()
t.sleep(1)
# 2021년 클릭
browser.find_element(By.XPATH,'//*[@id="conts"]/div[3]/div[2]/div/div/ul/li[3]/a').click()
t.sleep(2)

target_2021_title=browser.find_elements(By.CLASS_NAME,'rank01')
target_2021_name=browser.find_elements(By.CLASS_NAME,'rank02')
target_2021_like=browser.find_elements(By.CLASS_NAME,'cnt')

dict2={'rank2021':range(1,51),
       'title':makeString(target_2021_title,50),
       'name':makeString(target_2021_name,50),
       'like':makeInt(target_2021_like,50)}
col2=['rank2021','title','name','like']
df2=pd.DataFrame(dict2,columns=col2,index=range(50))

df2.to_csv("2021차트.csv",mode='w', index=False, encoding='utf-8-sig')

dfAll1 = pd.merge(df1,df2,left_on='rank2020',right_on='rank2021')
dfAll1.to_csv("2020-2021차트1.csv",mode='w', index=False, encoding='utf-8-sig')

dfAll2 = pd.merge(df1,df2, how='outer')
dfAll2.to_csv("2020-2021차트2.csv",mode='w', index=False, encoding='utf-8-sig')


plt.rcParams['font.family']='malgun gothic'

print(' # 1. 2020년도 차트 순위 DataFrame 입니다.')
t.sleep(2)
print(df1)
t.sleep(2)
print(' # 1-2. 2020년도 가장 많은 좋아요를 받은 가수입니다.')
t.sleep(2)
print(df1.groupby('like')['name'].max().iloc[-1])
t.sleep(2)
print(' # 1-3. 2020년도 1~50위 등록 상위 5명입니다.')
t.sleep(2)
print(df1['name'].value_counts()[:5])

plt.figure()
label1 = df1['name'].value_counts()[:5].index
values1 = df1['name'].value_counts()[:5].iloc[:]
x1=np.arange(len(label1))
plt.bar(x1,values1)
plt.xticks(x1, label1)
plt.show()

t.sleep(2)
print(' # 2. 2021년도 차트 순위 DataFrame 입니다.')
t.sleep(2)
print(df2)
t.sleep(2)
print(' # 2-2. 2021년도 가장 많은 좋아요를 받은 가수입니다.')
t.sleep(2)
print(df2.groupby('like')['name'].max().iloc[-1])
t.sleep(2)
print(' # 2-3. 2021년도 1~50위 등록 상위 5명입니다.')
t.sleep(2)
print(df2['name'].value_counts()[:5])


plt.figure()
label2 = df2['name'].value_counts()[:5].index
values2 = df2['name'].value_counts()[:5].iloc[:]
x2=np.arange(len(label2))
plt.bar(x2,values2)
plt.xticks(x2, label2)
plt.show()

t.sleep(2)
print(' # 3. 전체 가수의 좋아요 수 평균입니다..')
t.sleep(2)
print(dfAll2['like'].sum()/len(dfAll2.index))
t.sleep(2)


while True:
    search = input("검색하기\n"
               "2020년도 or 2021년도 :")
    if search != '2020년도' and search != '2021년도' and search != '2020' and search != '2021' :
        print('다시입력')
        continue
    else:
        if search == '2020' or search == '2020년도':
            search2 = input('가수 검색 or 순위 검색')
            if search2 == '가수 검색':
                search3 = input('가수명 입력: ')
                result = df1['name']== search3
                result = result.to_list()
                if True in result:
                    print(df1.loc[result,['rank2020','title']])
                else:
                    print('다시입력')
            elif search2 == '순위 검색':
                search3 = input('순위 입력: ')
                result = df1['rank2020']== int(search3)
                result = result.to_list()
                print(result)
                if True in result:
                    print(df1.loc[result,['name','title']])
                else:
                    print('다시 입력')
            else:
                print('다시입력')
                continue
        else:
            search2 = input('가수 검색 or 순위 검색')
            if search2 == '가수 검색':
                search3 = input('가수명 입력: ')
                result = df2['name']== search3
                result = result.to_list()
                if True in result:
                    print(df2.loc[result,['rank2021','title']])
                else:
                    print('다시입력')
            elif search2 == '순위 검색':
                search3 = input('순위 입력: ')
                result = df2['rank2021']== int(search3)
                result = result.to_list()
                if True in result:
                    print(df2.loc[result,['name','title']])
                else:
                    print('다시 입력')
            else:
                print('다시입력')
                continue