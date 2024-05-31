def user_info(*args):
    print(args)
    return args


user_info("TOM")
user_info("TOM", 18)


def user_info(**args):
    print(args)


user_info(name='TOM', age=18, id=10)


def sum(*nums):
    result = 0
    for n in nums:
        result += n
        print(result)


sum(123, 456, 789, 10, 20, 30, 40)
