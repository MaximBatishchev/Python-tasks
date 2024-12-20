a = input().lower()
if a == 'январь' or a == 'март' or a == 'май' or a == 'июль' or a == 'июль' or a == 'август' or a == 'октябрь' or a == 'декабрь':
    print(31)
elif a == 'февраль':
    print('28 или 29')
elif a == 'апрель' or a =='июнь' or a == 'сентябрь' or a == 'ноябрь':
    print(30)
else:
    print('Это не является месяцем')