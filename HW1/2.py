import os


def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с 
    вложенными структурами.
    """
    directory_content = []
    for content in os.listdir(sPath):
        name = os.path.join(os.path.abspath(sPath), content)
        if os.path.isfile(name):
            directory_content.append((os.path.abspath(sPath), content))
        else:
            print_directory_contents(name)
    print(directory_content)


print_directory_contents('C:\PyProjects\python_for_interviews\HW1')
