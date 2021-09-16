import os.path


def writer():
    if os.path.exists(name):
        print('Файл с данным названием существует, перезаписываем. ')
    with open(name, 'w', encoding='utf-8') as f:
        numbers = [i for i in range(1, 11)]
        strings = ['a'*i for i in range(1, 11)]
        for (n, s) in zip(numbers, strings):
            f.write(f'{n} {s}\n')
    reader()


def reader():
    with open(name, 'r', encoding='utf-8') as f:
        print(f.read())


name = input('Как будет называться файл? ')
name += '.txt'
writer()
