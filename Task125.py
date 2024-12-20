from random import randrange
def createDeck():
 cards = []
 for suit in ["s", "h", "d", "c"]:
      for value in ["2", "3", "4", "5", "6", "7", "8", "9", \
 "T", "J", "Q", "K", "A"]:
              cards.append(value + suit)
 return cards
def shuffle(cards):
 for i in range(0, len(cards)):
     other_pos = randrange(i, len(cards))
 temp = cards[i]
 cards[i] = cards[other_pos]
 cards[other_pos] = temp
def main():
 cards = createDeck()
 print("Исходная колода карт: ")
 print(cards)
 print()
 shuffle(cards)
 print("Перетасованная колода карт: ")
 print(cards)
if __name__ == "__main__":
 main()
