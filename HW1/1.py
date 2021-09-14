# постоянно преобразовывал (visual studio code) лямбду в эту функцию при сохранении, суть лямбды понял, хоть и запихнуть в join сам принт, вроде)
def stringifier(x): return ' '.join(x)


def chart(a, b):
    """
    Создаёт таблицу умножения от 2 до a и b
    """
    row = []
    for i in range(a-1):
        for j in range(b-1):
            row.append(str((i + 2) * (j + 2)))
        print(stringifier(row))
        row = []


chart(int(input('Введите первое число: ')),
      int(input('Введите второе число: ')))
