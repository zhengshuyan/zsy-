# a = float(input('请输入'))
# b = float(input('请输入另一个'))
# print('%.2f - %.2f =%.2f'%(a,b,a-b))
# a = 'a'
# print(ord(a))
# a = 98
# print(chr(a))
# email = '666@qq.com'
# for e in email:
    # o = ord(e) - 10
    # print(chr(o),end="")
    # print()
# year = int(input('请输入一个年份'))
# if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
#     print('%d是闰年'%year)
# else:
#     print('%d不是闰年'%year)2019
# val = input('请输入带温度表示符号的温度值')
# if val[-1] in ['C','c']:
#     f=1.8*float(val[0:-1])+32
#     print('转换后的温度为：%.2fF')
# elif val[-1] in ['F','f']:
#     c=(float(val[0:-1]-32)/1.8)
#     print('转换后的温度为:%.2fC'%c)
# else:
#     print('输入错误')
# F = float(input('输入华氏度'))
# C = (F-32)/1.8
# print('%.2f 摄氏度'%C)
# Number = input('请输入一个数字:')
# bai = int (Number [0])
# shi = int (Number [1])
# ge = int (Number [2])
# if bai**3+shi**3+ge**3 == int(Number):
#     print('是水仙花数')
# else:
#     print('不是水仙花数')
# 1.
# C = float(input('输入摄氏温度'))
# F = (9/5)*C + 32
# print('%.2F 华氏度' %F)
# 2.
import math 
print ('输入第一个坐标:')
x1 = float(input('>'))
y1 = float(input('>'))
print ('输入第二个坐标:')
x2 = float(input('>'))
y2 = float(input('>'))
radius = 6371.01
math.radians = float(input('输入地球表面的经度:'))
math.arccoss = float(input('输入地球表面的纬度:'))
d = math.radians * math.arccos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1-y2))
print ('%.2f',d)
