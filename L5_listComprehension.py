"""
n, n*n, map, lambda
list_comp - if, filter
双重循环
字典解析式
"""

# l = []
#
# for i in range(1,11):
#     l.append(i)
# print(l)

l_comp = [n for n in range(1,11) if n%2==0]
print(l_comp)

l_comp1 = [n*n for n in range(1,11)]
print(l_comp1)

l_map = list(map(lambda n: n*n,l_comp)) # lambda 匿名函数
print(l_map)

l_filter = list(filter(lambda n: n%2==0,l_comp))
print(l_filter)

l_double = []
for i in 'abc':
    for j in range(2):
        l_double.append((i, j))
print(l_double)

l_double_comp = [(i, j) for i in 'abc' for j in range(2)]
print(l_double_comp)

features = ['location', 'temperature', 'humidity', 'AQI']
values = ['Office', 28.5, 55.1, 78]

my_dict = {}
for feature, value in zip(features, values):
    my_dict[feature] = value
print(my_dict)

my_dict_comp = {feature: value for feature, value in zip(features,values)}
print(my_dict_comp)
