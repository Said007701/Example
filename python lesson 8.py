# представлено 2 выражения
# A.
# lst_1=[1,5,91]
# lst_2=[1,5,91]
# b.
# tpl_1=(1,5,91)
# tpl_2=(1,5,91)
# в чем разница между объектами в каждом из выражения?
# anwers:
# разные массывы
import random

# tpl=(1,2,2,3,1,2,4,3,2,2)
# print(tpl.count(2))

# a=()
# b=tuple()

# a = ("one")
# b=tuple([12])
# print(a,b)

# a=(1,2,3)
# b=1,2,3
# c=tuple([1,2,3])
# print(a,b,c)

# tpl_1 = (1, 5, 91)
# tpl_2 = list(tpl_1)
# tpl_2[2] = "web developer"
# tpl_2 = tuple(tpl_2)
# print(tpl_2)

# import random
# a=[random.randint(0,10) for i in range(10)]
# a=[1,2,3,4,5,6,7,8,9,10]
# print(a)
#
# b=int(input("Введите число? "))
#
# r=False
#
# for i in range(0,len(a)):
#     if a[i] == b:
#         r=True
#         break
#
# if r == True:
#     print("Элемент есть в списке")
# else:
#     print("Элемент в списке отсутствует")

# a=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]
# print(a[0][0])
# print(a[1][1])
# print(a[2][1])


# a=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]

# for i in range(len(a)):
#     print(len(a[i]))
    # for x in range(len(a[i])):
    #     print(a[i][x],end=" ")
    # print()

# n=int(input("Vivodite chislo strok: "))
# m=int(input("Viivodite chislo element v stroke: "))
# a=[]
#
# for i in range(n):
#     row = []
#     for i in range(m):
#         row.append(random.randint(0,10))
#     a.append(row)
#
# for i in range(len(a)):
#      print(len(a[i]))
#      for x in range(len(a[i])):
#          print(a[i][x],end=" ")
#      print()
