m = int(input())
DT= int(input())
C = 4186
q = m * C * DT
print('Для нагрева воды массой', m, 'потребуется', q, 'Дж')
KVatCH = q / 3600000
print(KVatCH * 8.9, 'центов')