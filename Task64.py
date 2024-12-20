prices = [4.95, 9.95, 14.95, 19.95, 24.95]
new_prices = [round(i * 0.4, 2) for i in prices]

print("Товар | Старая цена | Новая цена")
for i in range(len(prices)):
    print(f"Товар {i + 1} | ${prices[i]} | ${new_prices[i]}")