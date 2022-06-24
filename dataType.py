# <<자료형>>
# 1. 숫자
print('\n숫자')
num1 = 1
num2 = 2
print(num1, num2)
print(num1 + num2)
print(num1 * 2)
'''
결과:
숫자
1 2
3
2
'''

# 2. 문자열
print('\n문자열')
str1 = "Hello"
str2 = "World"
print(str1, str2)
print(str1 + str2)
print(str1 * 3)
print('str1[2]', str1[2])
print('str1[-1]', str1[-1])
print('str1[0:2]', str1[0:2])
print('str1[:]', str1[:])
print('str1[:-1]', str1[:-1])
print('str1[2:-1]', str1[2:-1])
print('str1[10:-1]', str1[10:-1])
'''
문자열
Hello World
HelloWorld
HelloHelloHello
str1[2] l
str1[-1] o
str1[0:2] He
str1[:] Hello
str1[:-1] Hell
str1[2:-1] ll
str1[10:-1] 
'''

# 3. 리스트
print('\n리스트')
li1 = ['사과', '오렌지', '귤']
li2 = ['배', '감']
print(li1)
print(li1, li2)
print(li1 + li2)
print(li1 * 2)
print(li1[0])
print(li1[1:2])
'''
리스트
['사과', '오렌지', '귤']
['사과', '오렌지', '귤'] ['배', '감']
['사과', '오렌지', '귤', '배', '감']
['사과', '오렌지', '귤', '사과', '오렌지', '귤']
사과
['오렌지']
'''

# 4. 튜플
print('\n튜플')
tu1 = (1, 2, 3)
tu2 = (4, 5)
print(tu1)
print(tu1, tu2)
print(tu1 + tu2)
print(tu1 * 2)
print(tu1[1])
print(tu1[:])
'''
튜플
(1, 2, 3)
(1, 2, 3) (4, 5)
(1, 2, 3, 4, 5)
(1, 2, 3, 1, 2, 3)
2
(1, 2, 3)
'''

# 5. 딕셔너리
print('\n딕셔너리')
dic1 = {'고양이': '야옹', '개': '멍멍', '오리': '꽥꽥'}
dic2 = {'돼지': '꿀꿀', '소': '음메'}
print(dic1)
print(dic1, dic2)
# print(dic1 + dic2) # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# print(dic1 * 2) # TypeError: unsupported operand type(s) for *: 'dict' and 'int'
print(dic1['고양이'])
# print(dic1.고양이) # AttributeError: 'dict' object has no attribute '고양이'
# print(dic1[0]) # KeyError: 0
# print(dic1[:]) # TypeError: unhashable type: 'slice'
print(dic1.keys())
print(dic1.values())
print(dic1.items())
# print(dic1.keys()[0]) # TypeError: 'dict_keys' object is not subscriptable
# print(dic1.values()[0]) # TypeError: 'dict_values' object is not subscriptable
# print(dic1.items()[0]) # TypeError: 'dict_items' object is not subscriptable
'''
딕셔너리
{'고양이': '야옹', '개': '멍멍', '오리': '꽥꽥'}
{'고양이': '야옹', '개': '멍멍', '오리': '꽥꽥'} {'돼지': '꿀꿀', '소': '음메'}
야옹
dict_keys(['고양이', '개', '오리'])
dict_values(['야옹', '멍멍', '꽥꽥'])
dict_items([('고양이', '야옹'), ('개', '멍멍'), ('오리', '꽥꽥')])
'''

# 6. 데이터프레임
'''
import는 파일 상단에 사용해야 하나 여기서는 DataFrame과 Series 때문에 사용했음을 명확히 설명하기 위해 중간에 사용함
pandas 설치 후 사용 가능, 빨간줄 그어진 pandas에 커서 두고 Alt+Enter => install package pandas 클릭
'''
import pandas as pd
print('\n데이터프레임')
df1 = pd.DataFrame(li1)
df2 = pd.DataFrame(tu1)
df3 = pd.DataFrame(dic1, index=[0])
df4 = pd.DataFrame(dic1, index=['소리'])
print(df1)
print(df2)
print(df3)
print(df4)
print(df1, df2)
# print(df1 + df2) #TypeError: can only concatenate str (not "int") to str
print(df1 * 2)
print(df4['고양이'])
print(df4.개)
'''
데이터프레임
     0
0   사과
1  오렌지
2    귤
   0
0  1
1  2
2  3
  고양이   개  오리
0  야옹  멍멍  꽥꽥
   고양이   개  오리
소리  야옹  멍멍  꽥꽥
     0
0   사과
1  오렌지
2    귤    0
0  1
1  2
2  3
        0
0    사과사과
1  오렌지오렌지
2      귤귤
소리    야옹
Name: 고양이, dtype: object
소리    멍멍
Name: 개, dtype: object
'''

# 7. 시리즈
print('\n시리즈')
ser1 = pd.Series(li1)
ser2 = pd.Series(tu1)
print(ser1)
print(ser2)
print(ser1, ser2)
# print(ser1 + ser2) # TypeError: can only concatenate str (not "int") to str
print(ser1 * 2)
print(ser1.values)
print(ser1.index)
'''
시리즈
0     사과
1    오렌지
2      귤
dtype: object
0    1
1    2
2    3
dtype: int64
0     사과
1    오렌지
2      귤
dtype: object 0    1
1    2
2    3
dtype: int64
0      사과사과
1    오렌지오렌지
2        귤귤
dtype: object
['사과' '오렌지' '귤']
RangeIndex(start=0, stop=3, step=1)
'''

# 8. 자료형 확인
print('\n자료형 확인')
print(type(li1))
print(type(df1))
print(df1.dtypes)
'''
자료형 확인
<class 'pandas.core.series.Series'>
<class 'list'>
<class 'pandas.core.frame.DataFrame'>
0    object
dtype: object
'''
