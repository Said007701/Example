# a=[1,2,3,4,5,6,7,8,9,10]
# b=filter(lambda num: num%2==0,a)
# print(list(b))
#
# a=[1,2,3,4,5,6,7,8,9,10]
# b=filter(lambda num: num%2==1,a)
# print(list(b))

# lst=['abcd','ab','c','de','bc']
# b=filter(lambda num:len(num)==2,lst)
# print(list(b))

# for x in lst:
#     if len(x)==2:
#         print(x)

# num = 4
# def func():
#     global num
#     num*=2
#     return num
# print(func())

# num=10
# def func():
#     global num
#     num-=3
#     return num
# print(func())

# import sys
# import matplotlib
# matplotlib.use('Agg')
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# ypoints = np.array([3, 8, 1, 10])
#
# plt.plot(ypoints, linestyle = 'dotted')
# plt.show()
#
# #Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()

# def get_Info(txt, func):
#     print(func(txt))
#
#
# def func(name):
#     return 'user name is ' + name
#
#
# get_Info('said', func)