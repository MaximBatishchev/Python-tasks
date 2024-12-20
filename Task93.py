WIDTH = 80
def center(s, width):
 if width < len(s):
   return s
 spaces = (width - len(s)) // 2
 result = " " * spaces + s
 return result
def main():
 print(center("Даже не знаю", WIDTH))
 print(center("что", WIDTH))
 print(center("сказать", WIDTH))
 print()
 print("Как дела?...")
main()