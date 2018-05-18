'''
print
mulitlines打印分段
len
slice [0] [0:b] [:b] [a:]
string methods: lower, count, index, find, replace
字符串连接（+，+' '+， .format, fstring）
dir, help()
'''

print('hello world')
message = 'Hello World'
print(message)


# mulitlines = '''I like Python,
# Python is awesome.
# '''
# print(mulitlines)

# len()
print('message一共有： ', len(message))
print(message[0])
print(message[0:5])  # 左闭右开
print(message[:5])
print(message[6:])

low = message.lower()
print(low)

print('l在message里出现的次数是：', message.count('l'))

# index, find都是查找字符的index；区别：index找不存在的字符时，会直接报错；但是find会返回-1
print(message.index('l'))
print(message.find('l'))
# print(message.index('x'))
print(message.find('x'))

newMessage = message.replace('World', 'python')
print(newMessage)

greeting = 'Hello'
name = 'Michael'

print(greeting + name)
print(greeting + ' ' + name + '. Welcome')
print('{0} {1}. Welcome'.format(greeting, name))
print(f'{greeting} {name}. Welcome')    # Python 3.6以后引入的方法

print(help(str))

print(type(3))
print(type(3.14))
print(3/2)
print(3//2) #除法取整
print(3**2)
print(7%2)
num = 1
# Python里没有++和--
num += 1
print(num)

strNum1 = '100'
strNum2 = '200'
print(strNum1 + strNum2)
print(int(strNum1) + int(strNum2))
