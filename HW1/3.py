"""3. Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации (нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря."""
import random


def generator(min_num, max_num, elems_num):
    """
    создаёт рандомные числа от min_num до max_num в количестве elems_num и кладёт их в список и, нумерует в словаре
    """
    elems = []
    elems_dict = {}
    for i in range(elems_num):
        elems.append(random.randint(min_num, max_num))
        elems_dict[i+1] = elems[i]
    return elems, elems_dict


print(generator(50, 60, 5))
