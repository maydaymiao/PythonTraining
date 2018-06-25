from module import my_module
# import my_module as mm
# from my_module import test
import random
import calendar
import datetime
import os
import sys

l = ['a', 'b', 'c', 'd']

index = my_module.find_index(l, 'c')
print(index)

print(random.randint(1,10))
print(calendar.isleap(2001))
print(datetime.datetime.today())
print(os.getcwd())
print(os.__file__)
print(sys.path)
