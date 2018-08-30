print('Hello world')
#
# score = 30
# if score>20:
#     print('222')
#
#     77+1
#
# print ("hello world")
#
# if True:
#     print ("Answer")
#     print ("True")
# else:
#         print ("Answer")
# print ("False")
#
# total = 11+ \
# 12+ \
# 13
# print(total  );
#
# print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')
#
# str = 'Runoob'
#
# print(str)  # 输出字符串
# print(str[0:-1 ])



# import sys;
# x = 'runoob';
# sys.stdout.write(x + '\n')

# import sys; x = 'runoob'; sys.stdout.write(x )
#
# input("\n按下 enter 键后退出。")
#
# x="a"
# y="b"
# # 换行输出
# print( x )
# print( y )
#
# print('---------')
# # 不换行输出
# print( x, end="" )
# print( y, end="" )
# print()

# from sys import *
# print('================Python import mode==========================');
# print ('命令行参数为:')
# for i in argv:
#     print ("111"+i)
# print ('\n python 路径为',path)

# a, b, c, d = 20, 5.5, True, 4+3j
# print(type(a), type(b), type(c), type(d))
#
# list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
# tinylist = [123, 'runoob']
#
# list.append(12)
# list[1] = 123
#
# tuple  = ( 'abcd', 786 , 2.23, 'runoob', 70.2,list )
# list.append(12)
# print(tuple)
# print(list)
# !/usr/bin/python3

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)
print(a - b)  # a和b的差集

print(a | b)  # a和b的并集

print(a & b)  # a和b的交集

print(a ^ b)  # a和b中不同时存在的元素