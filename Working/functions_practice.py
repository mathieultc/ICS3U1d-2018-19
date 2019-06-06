word = input()
length = len(word)
n_p = word.count("p")
last = word.rindex("p")

if n_p <= 2:
  print(word.rfind("p"))

elif n_p > 2:
  print(word[0:last].rfind("p"))

elif word.count("p") == 0:
    print(-2)