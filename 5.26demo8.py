def factorial(n):
    if n == 1:
        return 1  # 边界
    else:
        return n * factorial(n - 1)  # 递归函数


# 测试

num = 5
result = factorial(num)
print(f"The factorial of {num} is:{result}")

n = int(input())

def f(x):
    if x == 1:
        return x
    else:
        return (f(x-1)+1)*2
print(f(n))
