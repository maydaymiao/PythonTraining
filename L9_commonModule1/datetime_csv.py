'''
datetime https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
'''

import datetime
import pytz
import csv

# # print(datetime.date(2018,6,29))
# today = datetime.date.today()
# print(today)
# tdelta = datetime.timedelta(days=7)
# print(tdelta)
# print('7天后的日期是：', today+tdelta)
#
# print('今天是星期',datetime.date.weekday(today)) # weekday -> Monday 0
# print('今天是星期',datetime.date.isoweekday(today))  # isoweekday -> Monday 1
#
#
#
# t_bir = datetime.date(2019,2,9)
# t_till = t_bir - today
# print(f'距离下一次生日还有{t_till}天')
#
# print(datetime.datetime(2018,6,29,12,40,36,100000))
# t_time = datetime.datetime.today()
# print(t_time)
#
# # print(t_time+tdelta)
#
# # strftime把datetime转换成string
# print(datetime.datetime.strftime(t_time, '%B %d, %Y'))
#
# # strprtime把string转换成datetime
# t_str = 'June 29, 2018'
# print(datetime.datetime.strptime(t_str, '%B %d, %Y'))


with open('RealEstate.csv', 'r') as csv_file:
    contents = csv.reader(csv_file)
    # generator
    next(contents)
    for line in contents:
        print(line[0])

    # contents = csv.DictReader(csv_file)
    # for line in contents:
    #     print(line['street'])

