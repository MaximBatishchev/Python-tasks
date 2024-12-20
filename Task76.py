phrase = (input("Введите фразу для проверки: ")).lower()
new_phrase = ''
for char in phrase:
    if char.isalpha():
        new_phrase += char
result = "Палиндром"
for i in range(0, int(len(new_phrase)/2)):
    if new_phrase[i] != new_phrase[len(new_phrase)-i-1]:
        result = 'Не является палиндромом'
        break
print(result)