def gcd(n, m):
 d = min(n, m)
 while n % d != 0 or m % d != 0:
     d = d - 1
 return d
def reduce(num, den):
 if num == 0:
     return (0, 1)
     g = gcd(num, den)
     return (num // g, den // g)
     def main():
         num = int(input("Введите числитель дроби: "))
         den = int(input("Введите знаменатель дроби: "))
         (n, d) = reduce(num, den)
         print("Дробь %d/%d может быть сокращена до %d/%d." % (num, den, n, d))
     main()