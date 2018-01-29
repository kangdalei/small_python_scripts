# -*- coding: utf-8 -*-
# python3

# 本程序利用sha-512算法，由输入的初始字符串和给定的密钥长度（设定为
# 最小8位，最大64位），生成由ASCII码（10个数字、52个大小写字母、32
# 个特殊字符）组成的密钥。密钥看上去强度很高，但是用户选择的初始字符串一
# 般很简单，所以如果本程序被攻击者获得，那么可以很轻松的跑出专门针对本程
# 的彩虹表。实际上，所有利用简单字符串生成伪随机密钥的方法都有这个弱点，
# 需要对算法保密。

import hashlib


def sha512(str):
    """
    定义sha512函数，将输入的字符串，散列
    返回一个128位字符串（64字节16进制表示）
    """
    return hashlib.sha512(str.encode('utf-8')).hexdigest()


def digit2asc(n):
    """
    将任意整数转换为可见ASCII码，码值: 33-126，排除空格(32)
    对于单字节，小写字母出现频率低
    """
    return chr(n % 94 + 33)


i_str = input('请输入初始字符串<务必牢记>: ')
str = i_str  # 保留i_str值，将来打印用到

key_length = input('请输入密钥长度<直接Enter, 默认20位>: ')
if key_length == "":
    key_length = 20

try:
    key_length = int(key_length)
except ValueError:
    print('没有输入一个整数！已将密钥长度自动设为20！')
    key_length = 20

if key_length < 8:
    key_length = 8

elif key_length > 64:
    key_length = 64

# 根据密钥长度，将str转变为一个128位字符串
for i in range(0, key_length):
    str = sha512(str)

# str分成4组32位字符串，分别sha512散列后拼接成一个512位字符串
str4_sha512 = sha512(str[0:32]) + sha512(str[32:64]) + sha512(str[64:96]) \
              + sha512(str[96:128])

one_group_length = 512 // key_length

key_str = ""  # 口令初始字符串置空

for index in range(0, key_length):
    begin_position = index * one_group_length
    end_position = (index + 1) * one_group_length
    value = int(str4_sha512[begin_position:end_position], 16)
    key_str += digit2asc(value)

print("\n种子字符串 {} 的生成密钥({}位):\n ".format(i_str, key_length))
print(key_str)
