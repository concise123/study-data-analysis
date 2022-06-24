# 함수
def func1():
    print('매개변수랑 반환값 없는 함수입니다.')


def func2(input1, input2):
    output = input1 + input2
    return output


def func3(input1, input2):
    output1 = input1 + input2
    output2 = input1 * input2
    return output1, output2


func1()

num1 = 1
num2 = 2
add = func2(num1, num2)
print(f'{num1}과 {num2}의 합은 {add}입니다.')

num1 = 3
num2 = 4
add, mult = func3(num1, num2)
print(f'{num1}과 {num2}의 합은 {add}이고 곱은 {mult}입니다.')

num1 = 5
num2 = 6
result = func3(num1, num2)
print(f'{num1}과 {num2}의 합은 {result[0]}이고 곱은 {result[1]}입니다.')

'''
결과:
매개변수랑 반환값 없는 함수입니다.
1과 2의 합은 3입니다.
3과 4의 합은 7이고 곱은 12입니다.
5과 6의 합은 11이고 곱은 30입니다.
'''
