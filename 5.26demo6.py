def func_b():
    print("---b---")


def func_a():
    print("---a---")
    func_b()
    print("---c---")


func_a()


def fun1(x, y):
    print("这是函数一")
    sum = x + y
    return sum


def fun2():
    print("这是函数二")
    sum = fun1(2, 3)
    print(sum)


fun2()
