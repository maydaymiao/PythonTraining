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
