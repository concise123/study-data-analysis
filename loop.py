# 반복문
li = [1, 2, 3, 4, '가', '나', '다']

print('for문')

for i in li:
    print(i)
'''
1
2
3
4
가
나
다
'''
print('\n')

for i in li:
    print('1st', i)
    if i == 3:
        continue
    print('2nd', i)
'''
1st 1
2nd 1
1st 2
2nd 2
1st 3
1st 4
2nd 4
1st 가
2nd 가
1st 나
2nd 나
1st 다
2nd 다
'''
print('\n')

for i in li:
    print('1st', i)
    if i == 3:
        break
    print('2nd', i)
'''
1st 1
2nd 1
1st 2
2nd 2
1st 3
'''

print('\nwhile문')

num = 0
while num < 10:
    print(num)
    num += 1
'''
while문
0
1
2
3
4
5
6
7
8
9
'''