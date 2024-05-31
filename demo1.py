from tokenize import String

print('hello,Python!')
a = 100
b = 50
print(90)
print(a)
print(a * b)

print('北京欢迎你')
print("北京欢迎你")
print('''北京欢迎你''')
print("""北京欢迎你""")

a = 100
b = 50
print(a, b, '要么出众要么出局')
print(chr(98))
print('C')
print(chr(67))
print(8)
print(chr(56))
print('[')
print(chr(91))
print(ord('北'))
print(ord('京'))
print(chr(21271), chr(20140))
fp = open('note.txt', 'w')
print('北京欢迎你', file=fp)
print('北京欢迎你' + '2024')
my_name = input('请输入您的名字')
print('我的名字是' + my_name)

luck_number = input('请输入您的幸运数字:')

print('您的幸运数字是:' + luck_number)
# num = int(num)
# print('您的幸运数字是:' + num)
print(1, 2, 3)
fp = open('test.txt', 'w')
print(1, 2, 3, sep='---', end='<--->', file=fp)
fp.close()
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
true = '真'
rue = '真'
print('luck_number的数据类型是：', type(luck_number))
print(my_name, '的幸运数字是：', luck_number)

luck_number = '北京欢迎你'
print('luck_number的数据类型是：', type(luck_number))
no = number = 1024
print(no, number)
print(id(no))
print(id(number))
Pi = 3.1415926
PI = 3.1415926
num = 987
num2 = 0b1010101
num3 = 0o765
num4 = 0x87ABF
print(num)
print(num2)
print(num3)
print(num4)
a = 0.1
b = 0.2
print(round(a + b, 1), type(a + b))

x = 10
y = 10.0
print('x的数据类型：', type(x))
print('y的数据类型：', type(y))

x = 1.99E1413
print('科学计算法：', x, 'x的数据类型：', type(x))
x = 123 + 456j
print('实数部分:', x.real)
print('虚数部分：', x.imag)
print('hello\tooo')
print('hello\toooooo')
print('hellooooooo')
print('老师说：\'好好学习，天天向上\'')
print('北\n京\n欢\n迎你')
print(r'北\n京\n欢\n迎你')
print(R'北\n京\n欢\n迎你')
s = 'helloworld'
print(s[0], s[-10])
print('北京欢迎你'[4])
print('北京欢迎你'[-1])
print(s[2:7])
print(s[-8:-3])
print(s[:5])
print(s[5:])
x = '2022年'
y = '北京冬奥会'
print(x + y)
print(x * 10)
print(10 * x)

print('北京' in y)
print('上海' in y)

x = True
print(x)
print(type(x))
print(x + 10)
print(False + 10)
print('-' * 30)
print(bool(18))
print(bool(0), bool(0.0))

print(bool('北京欢迎你'))
print(bool(''))
print('-' * 30)
print(bool(False))
print(bool(None))
print('-' * 30)
x = 10
y = 3
z = x / y
print(z, type(z))

print('float类型转成int类型：', int(3.14))
print('-' * 30)
print('float类型转换为int类型：', int(3.14))
print('float类型转换为int类型：', int(3.9))
print('float类型转换为int类型：', int(-3.14))
print('float类型转换为int类型：', int(-3.9))

print('将int转成float类型:', float(10))
print('-' * 30)
print(int('100') + int('200'))
# print(int('18a'))
# print(float('45a.987'))
print('十进制转成十六进制:', hex(26472))
print('十进制转成八进制:', oct(26472))
print('十进制转成二进制:', bin(26472))
print('-' * 30)
s = '3.14+3'
print(s, type(s))
x = eval(s)
print(x, type(x))
print('-' * 30)
age = eval(input('请输入您的年龄：'))
print(age, type(age))

height = eval(input("请输入您的身高："))
print(height, type(height))

print('-' * 30)
hello = '北京欢迎你'
print(hello)
print(eval('hello'))
# print(eval('北京欢迎你'))
print('-' * 30)
print('加法：', 1 + 1)
print('减法：', 1 - 1)
print('乘法：', 2 * 3)
print('除法：', 10 / 2)
print('整除：', 10 // 3)
print('取余：', 10 % 3)
print('幂运算：', 2 ** 4)

x = 20
y = 10
x = x + y
print(x)
x += y
x -= y
print(x)
print('-' * 30)
x *= y
print(x)
x /= y
print(x)
print(type(x))
x %= 2
print(x)
print('-' * 30)
x %= 2
print(x)
z = 3
y //= z
print(y)

y **= 2
print(y)
print('-' * 30)
a = b = c = 100
print(a, b, c)
a, b = 10, 20
print(a, b)

print('-' * 30)
a, b = b, a
print(a, b)
print('-' * 30)
print('98大于90吗', 98 > 90)
print('98小于90吗', 98 < 90)
print('98等于90吗', 98 == 90)
print('98不大于90吗', 98 != 90)
print('98大于等于90吗', 98 >= 98)
print('98小于等于90吗', 98 <= 98)
print('-' * 30)
print(True and True)
print(True and False)
print(False and False)
print(False and True)
print('-' * 30)
print(True or True)
print(True or False)
print(False or False)
print(False or True)
print('-' * 30)
print(8 > 7 or 10 / 0)
print('-' * 30)
print(not True)
print(not False)
print(not (8 > 7))
print('按位与运算:', 12 & 8)
print('按位或运算:', 4 | 8)
print('按位异或运算符:', 31 ^ 22)
print('按位取反:', ~123)
print('左移位:', 2 << 2)
print('左移位:', 2 << 3)
print('右移位:', 8 >> 2)
print('右移位:', -8 >> 3)