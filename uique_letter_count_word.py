def unique_english_letters(word):
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
  count = 0
  counted = []
  for i in word:
    if i in counted and i in letters:
      count += 0
    elif i in letters and i not in counted: 
      counted.append(i)
      count += 1
  return count, counted