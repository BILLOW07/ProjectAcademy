vowels = "аеёиоуыэюя"
text = input("Введите строку: ")
print(''.join([vowels[(vowels.index(c.lower()) + 1) % 9].upper() 
      if c.lower() in vowels and c.isupper() else
      vowels[(vowels.index(c.lower()) + 1) % 9] 
      if c.lower() in vowels else c for c in text]))