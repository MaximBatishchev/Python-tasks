def countRange(data, mn, mx):
 count = 0
 for e in data:
       if mn <= e and e < mx:
           count = count + 1
 return count
def main():
 data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 print("Подсчитываем количество элементов в списке [1..10] между 5 и 7...")
 print("Результат: %d Ожидание: 2" % countRange(data, 5, 7))
 print("Подсчитываем количество элементов в списке [1..10] между –5 и 77...")
 print("Результат: %d Ожидание: 10" % countRange(data, - 5, 77))
 print("Подсчитываем количество элементов в списке [1..10] между 12 и 17...")
 print("Результат: %d Ожидание: 0" % countRange(data, 12, 17))
 print("Подсчитываем количество элементов в списке [] между 0 и 100...")
 print("Результат: %d Ожидание: 0" % countRange([], 0, 100))
 data = [1, 2, 3, 4, 1, 2, 3, 4]
 print("Подсчитываем количество элементов в списке", data, "между 2 и 4...")
 print("Результат: %d Ожидание: 4" % countRange(data, 2, 4))
main()