# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
# 首先，我们看看itertools提供的几个“无限”迭代器：
# import itertools
# this=itertools.count(1)
# for n in this:
#     print(n)


# cycle()会把传入的一个序列无限重复下去：
# import  itertools
# cs=itertools.cycle('ABC')#注意字符串也是序列的一种
# for n in cs:
#     print(n)

# import  itertools
# cs=itertools.cycle(["A","B","C"])
# for n in cs:
#     print(n)

# import  itertools
# cs=itertools.cycle({"name":"tianle","height":178})#只会循环key  不会循环value
# for n in cs:
#     print(n)

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
# import itertools
# db=itertools.repeat("A")
# for n in db:
#     print(n)

# import itertools
# db=itertools.repeat("A",3)
# for n in db:
#     print(n)
'''
无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：

'''
# import itertools
# natuals = itertools.count(1)
# ns=itertools.takewhile(lambda x: x<=10,natuals)
# print(list(ns))


# itertools提供的几个迭代器操作函数更加有用：
import itertools
for x in itertools.chain("ABC","DEF"):
    print(x)

# groupby()把迭代器中相邻的重复元素挑出来放在一起：
# for key,group in itertools.groupby("AAABBBCCCCCC"):#函数返回值作为组的key
#     print(key,list(group))
# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key,groud in itertools.groupby("AAaaAbBBBBbCcccCAAAAA",lambda x:x.upper()):#upper()函数是将字符串中的小写字母转换成大写字母
    print(key, list(groud))










