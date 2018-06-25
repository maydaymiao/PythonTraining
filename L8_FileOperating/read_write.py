'''
模式	可做操作	若文件不存在	是否覆盖
r	只能读	报错	        -
r+	可读可写	报错	        是
w	只能写	创建	        是
w+　	可读可写	创建         是
a　 只能写	创建	        否，追加写
a+	可读可写	创建	        否，追加写
'''

# f = open('test.txt', 'r')
# print(f.name)
# f.close()


# context manager
# with open('test.txt', 'r') as f:
    # contents = f.read()
    # print(contents)

    # contents = f.readlines()
    # print(contents)

    # contents = f.readline()
    # print(contents)

    # for line in f:
    #     print(line, end='')

    # size_to_read = 10
    # contents = f.read(size_to_read)
    # while len(contents)>0:
    #     print(contents, end='*')
    #     contents = f.read(size_to_read)

    # contents = f.read(5)
    # print(contents)
    # f.seek(0)
    # contents = f.read(5)
    # print(contents)

# with open('test2.txt', 'w') as f:
#     f.write('Testing..')


# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

with open('python.jpg', 'rb') as rf:
    with open('python_copy.jpg', 'wb') as wf:
        size_to_read = 4096
        contents = rf.read(size_to_read)
        while len(contents)>0:
            wf.write(contents)
            contents = rf.read(size_to_read)
