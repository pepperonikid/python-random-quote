import random

def foo():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  for i in range(5):
      rnd = random.randint(0, len(quotes)-1)
      print(quotes[rnd],end='')

  #f = open("quotes.txt")
  #quotes = f.readlines()
  #f.close()

  #print(quotes)py

if __name__== "__main__":
  foo()
