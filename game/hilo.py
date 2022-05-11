# Setup initial variables
# Start game function
# Check if player wants to continue playing
# have player 
# initial function must start player with 300 pts

#Alexander and Pume on initial and input




# from game.cards import Card
# import random


# class Hilo:
#     def __init__(self):

#         self.Card = []
#         self.is_playing = True
#         self.score = 0
#         self.total_score = 0
#         self.old_value = 0

#Start game by dealing out first card 
        # card = list(range(0,14))
        # for card in self.Card:
        #     random.shuffle(card)
        #     print (f"The card is: {card}")


    # def start_game(self):

    #     while self.is_playing:
    #         self.get_inputs()
    #         self.do_outputs()
    #         self.do_updates(self, self.guess, self.old_value)

    # def get_inputs(self):

    #     self.guess = input("Higher or lower? [h/l] ")
    #     deal_card = input("Play again? [y/n] ")
    #     self.is_playing = (deal_card == "y")
       
    # def do_updates(self, choice, old_value):

    #     if not self.is_playing:
    #         return 
    #     card = self.Card
    #     card.points(self, choice, old_value)
    #     self.score += card.points 
    #     self.total_score += self.score

    # def do_outputs(self):

    #     if not self.is_playing:
    #         return
        
    #     values = ""
    #     for i in range(len(self.dice)):
    #         die = self.dice[i]
    #         values += f"{die.value} "

    #     print(f"You rolled: {values}")
    #     print(f"Your score is: {self.total_score}\n")
    #     self.is_playing == (self.score > 0)
    
    # from unittest import result
from game.cards import Card
import random

# Card.h_l(result)
# Hilo.give_points(Card.h_l(result))

class Hilo:

  def __init__(self):
    self.play_game = True
    
    self.cards = Card()
    self.results = ""
    # self.game_in_play = True
    self.winner = None
    self.points = 300
    self.old_val = random.randint(1, 13)
       
  def give_points(self):
    if self.cards.result == "correct":
      self.points += 100
    if self.cards.result == "incorrect":
      self.points -= 75

    print(f"Your score is: {self.points}")

    return self.points
    
  def game_in_play(self, points):
    while points > 0:
      if(self.play_game):
        play = input("Wanna play? [y/n] ")
        if play == "y":
          self.play_game = True
          self.old_val = self.cards.h_l(self.old_val)
          points = self.give_points()   
        else:
          self.play_game = False
          print("\nThanks for playing.\n")
      
    else: 
      print("0 points left. Game over!")   
      return