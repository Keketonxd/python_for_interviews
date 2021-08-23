### Подготовка к собеседованию Python-разработчика

#### _Урок 1. Python - синтаксис языка, базовые структуры данных, функциональное программирование._

1. Написать функцию, реализующую вывод таблицы умножения размерностью AｘB. Первый и второй множитель должны задаваться в виде аргументов функции. Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле. После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку. Полученная строка выводится в главной функции. Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.
2. Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с 
    вложенными структурами.
    """
    
    заполните далее

3. Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации (нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
4. Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с аргументами. Клиент банка делает депозит на определенный срок. В зависимости от суммы и срока вклада определяется процентная ставка: 1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых). 10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых). 100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых). Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада. Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24). Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого срока. В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и выполнять расчет по нужной процентной ставке. Функция возвращает сумму вклада на конец срока.
5. Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную функцию подсчета процентов для пополняемой суммы. Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего. Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев. Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами), а главная функция — общую сумму по вкладу на конец периода.


#### _Урок 2. Python - парадигма ООП особенности и отличия от других ЯП._

1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке. Проверить работу программы, создав экземпляр (объект) родительского класса.
2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным. Результат выполнения заданий 1 и 2 должен быть идентичным.
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс. Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться переменная — скидка), и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).
6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.