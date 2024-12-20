user_input = input("Введите строку: ")
w = []
r = ""
for i in user_input:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z' or '0' <= i <= '9' or i == "'" or i == '-':
        r += i
    elif r:
        w.append(r)
        r = ""
if r:
    w.append(r)
print(w)