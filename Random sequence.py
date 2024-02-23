import random
import string
x=int(input("请输入您需要的位数："))
def generate_security_code(length):
    # 生成包括数字和大写字母的随机序列
    characters = string.ascii_uppercase + string.digits
    # 生成指定长度的随机序列
    code = ''.join(random.choice(characters) for _ in range(length))
    return code

security_code = generate_security_code(x) # 生成x位的防伪码
print(security_code)
