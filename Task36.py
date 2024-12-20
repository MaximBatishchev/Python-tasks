age = int(input())
if age < 0:
    print('Ошибка')
elif age == 1:
    print(10.5)
elif age == 2:
    print(21)
else:
    print(21 + (age - 2) * 4)