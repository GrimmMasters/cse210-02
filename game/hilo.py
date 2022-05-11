# Setup initial variables
# Start game function
# Check if player wants to continue playing
# have player 
# initial function must start player with 300 pts

#Alexander and Pume on initial and input

from game.cards import Card
import random

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
        self.old_val = self.cards.h_l(self.old_val)
        self.points = self.give_points()
        if self.points> 0:
          play = input("Play again? [y/n] ")
          if play == "y":
            self.play_game = True
            continue
          else:
            play == "n"
            self.play_game = False
            print("\nThanks for playing.\n")
            
        else:
            self.play_game = False
            print("\n0 points left. Game over!\n")
      
    else: 
      print("0 points left. Game over!")   
      return