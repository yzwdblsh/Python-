import random
# 全局变量和局部变量
# 全局变量:作用域是整个文件
# 局部变量:作用域是在上下文中最近的一整块同样缩进的Python语句
# 生成随机的银行卡号
def generate_card_number():
    # 银行卡号一般是16位数字
    card_number = '621' + ''.join(random.choices('0123456789', k=9))
    return card_number


# 创建1000个银行卡号和初始密码为 "000000" 的列表
bank_cards = [(generate_card_number()) for _ in range(10)]
bank_password = ['000000' for _ in range(10)]
my_dict = zip(bank_cards, bank_password)
# for _ in range(1000)
# print(dict)
# 输出1000个银行卡号和初始密码
# print("银行卡密码", "初始密码")
# 假设 my_dict 是通过 zip 函数创建的迭代器
for card, password in my_dict:
    print("银行卡号:", card, " 初始密码:", password)
"""
for card, password in my_dict:
    # dict = {generate_card_number(), '000000'}
    print(my_dict[card], my_dict[password])
    # keys = list(dict.keys())
    # values = list(dict.values)
    # print("银行卡号:",keys, " 初始密码:",values)"""
