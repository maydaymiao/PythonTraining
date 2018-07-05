import random
import os
import shutil

# print('0-1之间的随机浮点数：', random.random())
# print('0-10之间的随机整数：', random.randint(0,10))
# languages = ['C++', 'Python', 'VB', 'Java']
# ran_lan = random.choice(languages)
# print(ran_lan)
#
# colors = ['red', 'green', 'blue']
# ran_col = random.choices(colors, weights=[9,5,1], k=10)
# print(ran_col)
#
# poker = list(range(1,55))
# random.shuffle(poker)
# # print(poker)
# ran_pok = random.sample(poker, k=5) # random.sample是不会选到重复的元素
# print(ran_pok)

# print(os.getcwd())  # get current directories
# os.chdir(r'/Users/michael/Desktop')
# print(os.listdir())
# os.makedirs('os_learning/test')
# print(os.listdir())

# os.removedirs('os_learning/test')
# shutil.rmtree('os_learning')    # high level文件操作

'''
path = '/Users/michael/Desktop/dir'
├── file1.py
├── file2.py
├── subDir1_1
│   ├── subDir2_1
│   │   ├── subFile3_1.py
│   ├── subFile2_1.py
├── subDir1_2
│   ├── subFile2_2.txt
'''

# path = r'/Users/michael/Desktop/dir'
# for roots, dirs, files in os.walk(path):
#     print('Current root: ', roots)
#     print('Directories: ', dirs)
#     print('Files: ', files)
#     print('\n')

# print(os.path.basename(r'/Users/michael/Desktop/dir/file1.py'))
# print(os.path.dirname(r'/Users/michael/Desktop/dir/file1.py'))
# print(os.path.exists(r'/Users/michael/Desktop/dir/file1.py'))
# print(os.path.split(r'/Users/michael/Desktop/dir/file1.py'))
# print(os.path.splitext(r'/Users/michael/Desktop/dir/file1.py'))

