import itertools

def brute_force_password(password_length, possible_characters, actual_password):
    for length in range(1, password_length + 1):
        for guess in itertools.product(possible_characters, repeat=length):
            attempt = ''.join(guess)
            print("尝试密码:", attempt)
            if attempt == actual_password:
                return attempt
    return None

# 设置密码长度和可能的字符集合
password_length = 5
possible_characters = '0123456789'  # 假设密码是由数字组成的

# 要破解的密码
actual_password = '57899'

# 尝试破解密码
result = brute_force_password(password_length, possible_characters, actual_password)
if result:
    print("成功破解密码:", result)
else:
    print("未能破解密码.")