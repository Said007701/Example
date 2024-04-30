# a=(1,2,3,4,5)
# print(type(a))#class tuple
# print(a)#(1,2,3,4,5)

# b=tuple((1,2,3,4,5))
# print(type(b))# class tuple
# print(b)#(1,2,3,4,5)

# a=1,2,3,4,5
# print(a[3])

# a='a'
# b='b',
# print(type(a))#class str
# print(type(b))#class tuple

# my_tuple=(1,2,3,4,5)
# a, b, c, d, e =my_tuple
# print(c)# 3

# my_tuple=(1,2,3)
# a,_, __ =my_tuple
# print(__)#3

# my_tuple=(('a','b','c'),[1,2],((1,'a'),('b','c')))
# print(my_tuple[2][1])#('b','c')

# a=4,
# b=8,
# c='a',
# d='z',
# e=(14,'maximum','minimum')
# f=(14,'maximum','min')
# k=999,
# print(a<b)#True
# print(c<d)#True
# print(e>f)#True
# print(k<f)#False
# print(c<k)#TypeError: '<' not supported between instances of 'str' and 'int'

# x=(1,2,3,4)
# y=(5,6,7,8)
# z=x+y
# print(z)#(1,2,3,4,5,6,7,8)

# x=(1,2,3,4)
# z=x*3
# print(z)#(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

# student=(2007,'ivan','ivanov','9-A',False)
# del student

# a=(5,3,2,1,4)
# print(sorted(a))#[1, 2, 3, 4, 5]
# a=tuple(sorted(a))
# print(a)#(1, 2, 3, 4, 5)