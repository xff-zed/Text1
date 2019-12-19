# -*- coding: utf-8 -*-  
# 1.no system is safe 2.If you dare to do it, you can win. 3.Enjoyment in the virtual world as well as in the real world
# python 3.6.3, create time is 2019/11/8 8:55 GMT+8
# 创建空的集合
a = {1}
b = set()
print(a, type(a))  # dict
print(b, type(b))  # set

a = {1, 2, 3}
b = {3, 4, 5}
print(a - b)  # 1, 2
print(a | b)  # 1, 2, 3, 4, 5
print(a & b)  # 3
print(a ^ b)  # 1, 2, 4, 5

a = {1}
# 向集合中添加 数字2
a.add(2)  # a.update(2)
print(a)
# 同时添加 3, 4
a.update((3, 4))  #
print(a)

a = [1, 0, 0, 8, 6]
print(set(a))

