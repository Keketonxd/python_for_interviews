def num_check(num):
    check = False
    try:
        check = float(num)
    except ValueError:
        print('Это не число. ')
    if check:
        num = num.split('.')
        if len(num) == 1:
            print('Это целое число. ')
        else:
            print('Это нецелое число. ')
            print(int(num[0]) == int(num[1]))


number = input('Введите число: ')
num_check(number)
