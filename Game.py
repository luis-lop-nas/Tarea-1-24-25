class game:
    def __init__(self):
        self.player = None
        self.enemy = None
        self.turn = None
        self.game_over = False

    def start_game(self, Player, Enemy):
        print("Welcome to the game!")
        self.player = Player()
        self.enemy = Enemy()
        self.turn = "player"
        self.game_over = False

    def play_turn(self):
        if self.turn == "player":
            self.player.take_turn(self.enemy)
            if self.enemy.health <= 0:
                print("You defeated the enemy!")
                self.game_over = True
            else:
                self.turn = "enemy"
        else:
            self.enemy.take_turn(self.player)
            if self.player.health <= 0:
                print("You were defeated by the enemy!")
                self.game_over = True
            else:
                self.turn = "player"
    def end_game(self):
        print("Game over! Thanks for playing.") 
        self.game_over = True
    def run(self):
        self.start_game()
        while not self.game_over:
            self.play_turn()
        self.end_game()
