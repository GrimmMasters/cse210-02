
# initial function must display a random card from 1-13 and set to some variable
#
# 
# definition where the next card found
# compare old number to new number with high or low
# deal out points

import random

class Card:
  def __init__(self):
    
    self.card1 = 0
    self.card2 = 0
    self.guess = ""
    self.result = ""
    
    
    
  def h_l(self, old_val):
    self.card1 = old_val
    self.card2 = random.randint(1, 13)
    print(f"\nThe card is: {self.card1}")
    guess = input("Higher or lower? [h/l] ")
    print(f"Next card was: {self.card2}")
    
    if self.card1 < self.card2 and guess == "h":
      self.result = "correct"
    elif self.card1 > self.card2 and guess == "h":
      self.result = "incorrect"
    elif self.card1 > self.card2 and guess == "l":
      self.result = "correct"
    else:
      self.result = "incorrect"
    
    return self.card2


# import random

# class Card:

#     def __init__(self):
#         self.value = 0
#         self.points = 0


#     def deal(self):

#         self.value = random.randint(1,13)

#     def points(self, choice, Old_value):

#         if choice == 'h' and Old_value < self:
#             self.points = 100
#         elif choice == 'l' and Old_value > self:
#             self.points = 100
#         elif choice == 'l' or'h' and Old_value == self:
#             self.points = 0
#         else:
#             self.points = -75


