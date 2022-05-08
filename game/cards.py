
# initial function must display a random card from 1-13 and set to some variable
#
# 
# definition where the next card found
# compare old number to new number with high or low
# deal out points
import random

class Die:

    def __init__(self):
        self.value = 0
        self.points = 0

    def roll(self):

        self.value = random.randint(1,6)
        self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0