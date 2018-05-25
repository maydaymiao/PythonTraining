"""
list(列表), tuple（元祖）, set（集合）, dict（字典）

List: len(list), slice [0] [-1]
append, insert(position, object)
list1.insert(0, list2)
list1.extend(list2)
remove, pop, reverse, sort
min, max, sum
index, in
for .. in ..    for .., .. in enumerate()
join, split

Tuple

Set: intersection, difference, union
create empty list, tuple, set

Dict: get, update, del, pop
keys, values, items
"""

languages = ['C++', 'Python', 'Java', 'PHP']
print(languages)
print(len(languages))
print(languages[0])
print(languages[-1])
languages.append('Ruby')    # append把添加的元素放到最后一个
# print(languages)
languages.insert(1, 'C')
# print(languages)
languages2 = ['VB', 'JS']
# languages.insert(0, languages2)
# print(languages)
languages.extend(languages2)    # extend会把list的括号给去掉，再插入元素
print(languages)

languages.remove('PHP') # remove不会返回
popped = languages.pop()
print('popped: ',popped)
print(languages)

languages.reverse()
print(languages)
languages.sort()
print(languages)

lanSort = sorted(languages)
print(languages)
print(lanSort)

nums = [1,5,2,4,3]
print(f'min: {min(nums)}, max: {max(nums)}, sum: {sum(nums)}')

print(languages.index('Python'))    # 如果找不到元素，会直接报错
result = 'VB' in languages  # return false
print(result)

for language in languages:
    print(language)

for index, language in enumerate(languages, start=1):
    print(index, language)

strLan = ', '.join(languages)
print(strLan)
newList = strLan.split(', ')
print(newList)


## tuple只支持查询，不支持任何和修改相关的函数
# t1 = ('a', 'b', 'c')
# print(t1.index('b'))

# s1 = {'C++', 'Python', 'Java', 'PHP', 'Python'}
# s2 = {'Python', 'VB'}
# print(s1)
# print('Java' in s1)
# print('交集：',s1.intersection(s2))
# print('差集', s1.difference(s2))
# print('并集', s1.union(s2))

# l1 = []
# l2 = list()
#
# t1 = ()
# t2 = tuple()
#
# s1 = set()
#
# d1 = {}
# d2 = dict() # 字典

# 键值 key value
employee1 = {'name': 'Michael', 'age': 30, 'skill': ['Python', 'Lego']}
# print(employee1)
# print(employee1['name'])
# print(employee1['phone']) # 用这种方法，如果key不存在，则直接报错
# print(employee1.get('phone', 'Not Found'))
employee1['phone'] = '139123456'
# print(employee1)
# employee1.update({'gender': 'male', 'phone': '139'})
print(employee1)

# del employee1['phone']
# popped = employee1.pop('phone')
# print(popped)
# print(employee1)

# print(employee1['skill'][0])

print(employee1.keys())
print(employee1.values())
print(employee1.items())

for key, value in employee1.items():
    print(key, value)
