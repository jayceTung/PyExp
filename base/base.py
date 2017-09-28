# base.py
# coding:utf-8
import random
import time

#
# for letter in 'Python':     # 第一个实例
#    if letter == 'h':
#        continue
# print '当期字母 :', random.randint(0,99)
#
# dic = {1: 10, 2: 20}
# for num in range(0, 10):
#     print dic.get(num)
#
# ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print "当前时间 ：", ticks
#
#
# def express(string="default"):
#     print string
#     return
#
#
# express()
#


def expression(*vartuple):
    for var in vartuple:
        print var
        raise Exception("Invalid")
    return


try:
    expression(1, 2, 2, 2)
except Exception as e:
    print "1"


sum = lambda arg1, arg2: arg1 + arg2


print sum(1, 3)
