cents = int(input())
print(cents // 200)
cents %= 200
print(cents // 100)
cents %= 100
print(cents // 25)
cents %= 25
print(cents // 10)
cents %= 10
print(cents // 5)
cents %= 5
print(cents)