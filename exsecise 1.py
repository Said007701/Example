# a=(2,3,5,77,3,2,1)
# print(a[-1])

# a=(4,2,3,5,77,3,2,1,5)
# print(a[0])

# a=(2,3,5,77,3,2,1)
# print(a[0],a[-1])

# a=(2,3,5,77,3,2,1)
# print(len(a))

# a=(1,2,3,4,5,6,7,8,9,1)
# b=a[0]==a[-1]
# print(b)

# a=[1,2,3,4,5,6,7,8,9,1]
# def name(arg,arg2):
#     if arg==a[0]:
#         print(True)
#     else:
#         print(False)
#     if arg2==a[-1]:
#         print(True)
#     else:
#         print(False)
# name(1,9)


# if c==d:
#     print("True")
# else:
#     print("False")

# def name(*name):
#     a=(1,2,3,4,5,6,7,8,9,10)
#     b=a[0]==[-1]


# a=[1,2,3,4,5,6]
# print(a[0:3])

# a=int(input("a: "))
# b=int(input("b: "))
# if a % b ==0:
#     print(True)
# else:
#     print(False)

# a=("abcde")
# print(list(a))

# a={
#     "year":"2025-",
#     "month":"12-",
#     "day":"31",
# }
# print(a["year"],a["month"],a["day"])
#
# for x in range(1,100):
#     print(x)

# for x in range(-100,0):
#     print(x)


# for x in range(100,1,-1):
#     print(x)

# for x in range(1,100,2):
#     print(x)

# for x in range(1,100,3):
#     print(x)

# a=[1,2,3,4,5,6]
# print(a[4:6]),

# a=[1,2,3,4,5]
# print(a[0]+a[1]+a[2]+a[3]+a[4])
#
# a=[1,2,3,4,5]
# print(a[0]**2+a[1]**2+a[2]**2+a[3]**2+a[4])

# x={
#     "a":2,
#     "b":3,
#     "c":6,
#     "d":8,
# }
# for key in x:
#     x[key]*=2
# print(x)

# a="abcdf"
# a=a[::2]
# print(a)

# a=[1,2,3,4,5]
# a.reverse()
# print(a)

# for x in range(10,1000,5):
#     print(x)

# a='abcdeabc'
# b=(set(a))
# print(b)

# number=[1,-2,3,-4,-5,8,7]
# numbers=[num for num in number if num>0]
# print(numbers)

# a=[1.456,2.125,3.32,4.1,5.34]
# a=[round(num,1)for num in a]
# print(a)

# a={
#     "a":1,
#     "b":2,
#     "c":3,
#     "d":4,
# }
# print(a.values())

# a=list(range(0,10))
# print(a)

# tpl1=[1,2,3,4]
# tpl2=[5,6,7,8]
# print(tpl1+tpl2)

# a=list(range(1,10,2))
# print(a)

# tpl1=(1,2,3,4)
# tpl2=(5,6,7,8)
# print(tpl1+tpl2)

# dct1={
#     "a":1,
#     "b":2,
# }
# dct2={
#     "c":1,
#     "d":2,
# }
# dct1.update(dct2)
# print(dct1)

# a={1,2,3,4,5}
# b={4,5,6,7,8}
# c=a.intersection(b)
# print(c)

# a={1,2,3,4,5}
# b={4,5,6,7,8}
# c=a.symmetric_difference(b)
# print(c)

# txt='123451'
# txt1='45678'
# for i in txt:
#     for x in txt1:
#         if i == x:
#             print(i)

# for x in range(0,10,2):
#     print(str(x)*x)

# for i in range(0,10,2):
#     print(" " * ((9-i)//2)+str("*")*i)
#
# for i in range(0,10,2):
#     print(" " * ((9-i)//2)+str(i)*i)

# a=[
#     [11,12,13,14,15],
#     [21,22,23,24,25],
#     [31,32,33,34,35],
#     [41,42,43,44,45],
#     [51,52,53,54,55],
#
# ]
# for i in a:
#     print(i[2])
#
# a=1
# for x in range(1,10,2):
#     print(" "+"x"*a)
#     a+=2

# a=1
# for x in range(1,10,2):
#     print(" "+"x"*a)
#     a+=3

# for x in range(0,10):
#      print(str(x)*3)

# a=5
# for x in range(1,10,2):
#     print("  "+"x"*a)
#     a-=1


# for x in range(10,0,-1):
#     print(str(x)*x)

# events = [
#   {
#     'date':  '2019-12-29',
  #   'event': 'name1'
  # },
  # {
  #   'date':  '2019-12-31',
  #   'event': 'name2'
  # },
  # {
  #   'date':  '2019-12-29',
  #   'event': 'name3'
  # },
  # {
  #   'date':  '2019-12-30',
  #   'event': 'name4'
  # },
  # {
  #   'date':  '2019-12-29',
  #   'event': 'name5'
  # },
  # {
  #   'date':  '2019-12-31',
  #   'event': 'name6'
  # },
  # {
  #   'date':  '2019-12-29',
  #   'event': 'name7'
  # },
#   {
#     'date':  '2019-12-30',
#     'event': 'name8'
#   },
#   {
#     'date':  '2019-12-30',
#     'event': 'name9'
#   },
# ]
# mybox={}
# for event in events:
#     date=event["date"]
#     event_n=event["event"]
#     if date not in mybox:
#         mybox[date]=[event_n]
#     else:
#         mybox[date].append(event_n)
# print(mybox)

# events = [
#     {
#         'date': '2019-12-529',
#         'event': 'name1'
#     },
#     {
#         'date': '2019-12-3641',
#         'event': 'name1',
#     },
#     {
#         'date': '2019-12-329',
#         'event': 'name3',
#     },
#     {
#         'date': '2019-12-30',
#         'event': 'name1'
#     },
#     {
#         'date': '2019-12-229',
#         'event': 'name3'
#     },
#     {
#         'date': '2019-12-131',
#         'event': 'name3'
#     },
#     {
#         'date': '2019-12-129',
#         'event': 'name7'
#     },
#     {
#         'date': '2019-12-230',
#         'event': 'name7'
#     },
#     {
#         'date': '2019-12-430',
#         'event': 'name9'
#     },
# ]
# mybox={}
# for i in events:
#     date=i["date"]
#     event_n=i["event"]
#     if event_n not in mybox:
#         mybox[event_n]=[date]
#     else:
#         mybox[event_n].append(date)
# print(mybox)

# events = [
#             {
#     'date':  '2019-12',
  #   'event': 'name1'
  # },
  # {
  #   'date':  '2019-12',
  #   'event': 'name2'
  # },
  # {
  #   'date':  '2019-11',
  #   'event': 'name3'
  # },
  # {
  #   'date':  '2019-11',
  #   'event': 'name4'
  # },
  # {
  #   'date':  '2020-10',
  #   'event': 'name5'
  # },
  # {
  #   'date':  '2020-10',
  #   'event': 'name6'
  # },
  # {
  #   'date':  '2020-11',
  #   'event': 'name5'
  # },
  # {
  #   'date':  '2020-11',
  #   'event': 'name6'
  # },
  # {
  #   'date':  '2020-12',
  #   'event': 'name7'
  # },
  # {
  #   'date':  '2020-12',
  #   'event': 'name8'
  # },
  # {
  #   'date':  '2020-12',
  #   'event': 'name9'
#   },
# ]
#
# mybox={}
# for event in events:
#     date=event["date"]
#     event_n=event["event"]
#     if date not in mybox:
#         mybox[date]=[event_n]
#     else:
#         mybox[date].append(event_n)
# for x in mybox:
#     print(x,'\n', mybox[x],'\n')

