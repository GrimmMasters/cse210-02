
# initial function must display a random card from 1-13 and set to some variable
#
# 
# definition where the next card found
# compare old number to new number with high or low
# deal out points
import random

class Card:

    def __init__(self):
        self.value = 0
        self.points = 0


    def deal(self):

        self.value = random.randint(1,13)

    def Points(self, choice, Old_value):

        if choice == 'h' and Old_value < self:
            self.value = 100
        elif choice == 'l' and Old_value > self:
            self.value = 100
        elif choice == 'l' or'h' and Old_value == self:
            self.value = 0
        else:
            self.value = -75


