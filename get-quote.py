import random

def foo():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  rnd = random.randint(0, len(quotes)-1)
  f.close()

  print(quotes[rnd])

  #f = open("quotes.txt")
  #quotes = f.readlines()
  #f.close()

  #print(quotes)py

if __name__== "__main__":
  foo()
