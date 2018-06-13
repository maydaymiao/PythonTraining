"""
print, return, parameter, default parameter
leap year (month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
如果能被4整除，且不能被100整除，则为闰年
如果能被100整除，且能被400整除，则为闰年
year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
*args, **kwargs
"""

# def hello1():
#     print('hello1')
#
# hello1()

# def hello2():
#     return 'hello2'
#
# print(hello2())

# def hello3(name):
#     return f'Hello {name}'
#
# print(hello3('Michael'))

# def hello4(name, language='Python'):
#     return f'Hello {name}, you are learning {language}'
#
# print(hello4('Michael', 'Java'))

# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# def is_leap(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
# def month_cal(year, month):
#     if not 1 <= month <= 12:
#         return 'Invalid Month'
#     if month == 2 and is_leap(year):
#         return 29
#     return month_days[month]
#
# print(month_cal(2000, 4))

# def test(a, *args, **kwargs):
#     print('a: ', a)
#     if args:
#         print('args: ', args)
#     if kwargs:
#         print('kwargs: ', kwargs)
#         for feature, value in kwargs.items():
#             print(value)
#
# test(1,2,3,4,5,x=6,y=7)

