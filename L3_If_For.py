'''
if, elif, else
true, false, and, or
if not
==, is
break, continue
双重循环
range
while
'''


language = 'Python'
if language == 'Python':
    print('Python is awesome')

language = input('Please enter your choice: ')
if language == 'Python':
    print('Python is awesome')
elif language == 'Java':
    print('Java is cool')
else:
    print('Hello')

# Python中没有switch case

user = 'admin'
logged_in = True

if user == 'admin' and logged_in:
    print('Admin Page')
else:
    print('Bad cred')

logged_in = False
if not logged_in:
    print('Please log in')
else:
    print('Welcome')

a = 'Hello'
b = 'Hello'
print(a==b)
print(id(a))  # a和b在内存里是相同的地址
print(id(b))

c = [1,2,3]
d = [1,2,3]
print(c==d)
print(id(c))  # c和d在内存里是不同的地址
print(id(d))

nums = [1,2,3,4,5,6]
for num in nums:
    if num == 3:
        print('Found')
        # break # 满足条件，跳出循环
        continue # 满足条件，跳过当前条件，继续执行
    print(num)

nums = [1,2,3,4,5,6]
for num in nums:
    for letter in 'abc':
        print(num, letter)

for i in range(1,11):
    print(i)

x = 0
while x<10:
    print(x)
    x += 1

nums = [1,2,3,4,5]
i=0
while i<len(nums):
    print(nums[i])
    i+=1

for num in str:
    print(type(num))
