s = input("Введите строку: ")
characters = {}
for ch in s:
    characters[ch] = True
print("Строка содержит", len(characters), "уникальных символов.")