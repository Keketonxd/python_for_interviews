def in_tariffs(amount, months):
    """
    Функция для проверки наличия тарифов в банке по внесённой сумме 
    """

    if months not in [6, 12, 24]:
        return False

    tariffs = (
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
    )

    for tariff in tariffs:
        if tariff['begin_sum'] <= amount < tariff['end_sum']:
            return tariff[months]

    return False


def deposit(amount, months, fixed_sum):
    """
    Рассчитывает депозит по amount вложенных изначально средств, months месяцев вклада, и fixed_sum докладываемой сумме в конце месяца
    """
    rate = in_tariffs(amount, months)

    # Функция для расчёта процентов по дополнительным взносам(Считаем, что взносы идут все месяца кроме первого и последнего)
    def fixed_sum_percents(months_amount=months, sum=fixed_sum):
        total_amount = 0
        for _ in range(months_amount - 2):
            # Высчитываем пополнения фиксированные
            total_amount += sum
            # Начисляем на них процент (месячный -> в степени 1/12)
            total_amount *= ((1 + rate / 100) ** (1/12))
        return total_amount

    # Проверяем возможность внесения на данный срок
    if not rate:
        print('Нет подходящего тарифа')
    else:
        # Умножаем начальную сумму в зависимости от найденной процентной ставки и количества месяцев
        total = amount * ((1 + rate / 100) ** (months / 12)
                          ) + fixed_sum_percents()
        print(round(total, 2))


deposit(1000, 12, 100)
