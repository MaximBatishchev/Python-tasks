num = int(input())
sum = num // 1000 + num % 10 + num % 100 // 10 + num % 1000 // 100
print(sum)