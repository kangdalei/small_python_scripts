# -*- coding:utf-8 -*-
# 计算成盘状的钢板重量
# 圆盘, 单位m，wd外径，nd内径，hd厚度
# 用正则表达式检测输入格式是否正确

import re

print("通过外径内径厚度, 计算钢圆盘重量kg.")
print("输入q退出")

while True:
    tag = True
    while tag:
        wd = input('请输入圆盘外径(m)或(q退出): ')
        if re.match(r'^\d+\.*\d*$|^\.\d+$|^q$', wd):
            tag = False
        else:
            print("输入格式错误, 重新输入: ")

    if wd == 'q':
        break

    tag = True
    while tag:
        nd = input('请输入圆盘内径(m)或(q退出): ')
        if re.match(r'^\d+\.*\d*$|^\.\d+$|^q$', nd):
            tag = False
        else:
            print("输入格式错误, 重新输入: ")

    if nd == 'q':
        break

    tag = True
    while tag:
        hd = input('请输入圆盘厚度(m)或(q退出): ')
        if re.match(r'^\d+\.*\d*$|^\.\d+$|^q$', hd):
            tag = False
        else:
            print("输入格式错误, 重新输入: ")

    if hd == 'q':
        break

    wd = float(wd)
    nd = float(nd)
    hd = float(hd)

    sw = 7.85e3 * hd * 0.7854 * (wd**2 - nd**2)
    sw = round(sw, 2)
    print('钢圆盘重量 ' + str(sw) + ' kg')
