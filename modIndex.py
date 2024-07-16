# https://docs.python.org/3/py-modindex.html


import random

for i in range(3):
  print(random.random())

for i in range(3):
  print(random.randint(10,20))
  
  members = ['hyo','you','tion','seung']
  leader = random.choice(members)
  print(leader)
  
  
  #Dice
  class Dice:
    def roll(self):
      first=random.randint(1,6)
      second=random.randint(1,6)
      return first, second
    
dice = Dice()
print(dice.roll())