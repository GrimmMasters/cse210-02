# Setup initial variables
# Start game function
# Check if player wants to continue playing
# have player 
# initial function must start player with 300 pts

#Alexander and Pume on initial and input


from game.cards import Card


class Hilo:
    def __init__(self):

        self.Card = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0
        self.old_value = 0

        for i in range(5):
            die = Die()
            self.dice.append(die)

    def start_game(self):

        while self.is_playing:
            self.get_inputs()
            self.do_outputs()
            self.do_updates()

    def get_inputs(self):

        roll_dice = input("Roll dice? [y/n] ")
        self.is_playing = (roll_dice == "y")
       
    def do_updates(self, choice, ):

        if not self.is_playing:
            return 
        card = self.Card
        card.points()
        self.score += card.points 
        self.total_score += self.score

    def do_outputs(self):

        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)