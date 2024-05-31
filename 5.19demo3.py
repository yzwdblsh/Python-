import random


def cards(c, p):
    dic = dict(zip(c, p))
    print(dic.keys())
    print(dic.values())
    print(dic.items())
    return 0


card = ['621' + ''.join(random.choices('0123456789', k=9)) for _ in range(10)]
password = ['000000' for _ in range(1000)]
num = cards(card, password)
