n = 98
if not n % 2:
    print(n, '为偶数')

print('-----判断一个字符串是否是空字符串-------')
x = input('请输入一个字符串:')
if x:
    print('x是一个非空字符串')

if not x:
    print('x是一个空字符串')
print('--------表达式也可以是一个单纯的布尔型变量--------')
flag = eval(input('请输入一个布尔类型的值:True或者False'))
if flag:
    print('flag的值为True')

if not flag:
    print('flag的值为False')
print('------使用if语句时，如果语句中只用一句代码，可以将其放在一行')
a = 10
b = 5
amax = 0
if a > b: amax = a
print('a和b的最大值为：', amax)
