# print('Imported from my module...')

test = 'This is my first module'


def find_index(to_search, target):
    for index, value in enumerate(to_search):
        if value == target:
            return index
    return -1

def main():
    print(test)


if __name__ == '__main__':
    main()
