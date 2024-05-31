def cards():
    a = input("请输入一个数")
    d = int(a)
    b = input("请在输入一个数")
    e = int(b)
    c = d + e
    return c


print(cards())


def add(a, b):
    result = a + b
    print(f"{a}+{b}的结果为:{result}", "天气真好", sep='<-->', end='<>')
    print('asdfg')


add(5, 6)


def fun_default_parameters(param1, param2=2):
    print(param1 + param2)


fun_default_parameters(1)
fun_default_parameters(1, 5)
fun_default_parameters(param1=5, param2=3)
fun_default_parameters(param2=1, param1=10)


def fun_default_parameters(param1, param2=2):
    print(param1 - param2)
    return param1 - param2


fun_default_parameters(param2=1, param1=10)
print(fun_default_parameters(100, param2=2))
fun_default_parameters(5, param2=2)
# fun_default_parameters(param1=1,2)SyntaxError: positional argument follows keyword argument
