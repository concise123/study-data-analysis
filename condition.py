num = int(input('숫자를 입력하세요: '))

print('#1')

if num > 10:
    print("10보다 큼")

print('\n#2')

if num > 10:
    print("10보다 큼")
else:
    print("기타")

print('\n#3')

if num > 10:
    print("10보다 큼")
elif num > 5:
    print("5보다 큼")
else:
    print("기타")

'''
숫자를 입력하세요: 9
#1

#2
기타

#3
5보다 큼
'''