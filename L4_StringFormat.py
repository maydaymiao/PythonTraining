"""
{:02}, {:.2f}, {:,}
XX日 XX月，XX年，X weekday，is the X day of this year
https://docs.python.org/3/library/datetime.html
"""


# for i in range(1, 11):
#     print('the value is {:02}'.format(i))

# pi = 3.1415926
# print('pi is equal to {0:.3f}'.format(pi))
#
# print('1MB is equal to {:,} bytes'.format(1024*1024))


import datetime
print(datetime.datetime.now())
print('{0:%d %B, %Y, %A} is the {0:%j} day of this year'.format(datetime.datetime.now()))
