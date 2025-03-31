from Player import Player
from Opponent import Opponent
from Boss import Boss  

# The score attribute is already defined in the Game class's __init__ method.


class Game:
    def __init__(self):
        self.score = 0
        self.player = None
        self.opponent = None
        self.is_running = False

    def start(self):
        self.is_running = True
        self.score = 0
        print("Game started!")

    def update(self):
        if self.is_running:
            print("Game is updating...")
            # Add logic to update game state here
        else:
            print("Game is not running.")

    def end_game(self):
        self.is_running = False
        print("Game ended!")

    def reset(self):
        self.score = 0
        self.player = None
        self.opponent = None
        self.is_running = False
        print("Game has been reset.")

    def serialize(self):
        """
        Serializes the game state.
        :return: A dictionary representing the game state.
        """
        return {
            "score": self.score,
            "is_running": self.is_running,
            "player": self.player.serialize() if self.player else None,
            "opponent": self.opponent.serialize() if self.opponent else None
        }
    def deserialize(self, data):
        """"
        Deserializes the game state from a dictionary."
        """
        self.score = data["score"]
        self.is_running = data["is_running"]
        if data["player"]:
            self.player = Player()
            self.player.deserialize(data["player"])
        if data["opponent"]:
            self.opponent = Opponent()
            self.opponent.deserialize(data["opponent"])

    def __str__(self):
        """
        Returns a string representation of the game.
        :return: A string representing the game state.
        """
        return f"Game state: score={self.score}, running={self.is_running}, player={self.player}, opponent={self.opponent}"
    
    def convert_enemy_to_star(self, enemy):
        """
        Converts an enemy to a star and increments the score.
        :param enemy: The enemy to be converted.
        """
        if self.is_running and enemy:
            print(f"Enemy {enemy} converted to a star!")
            self.score += 1
        else:
            print("Game is not running or invalid enemy.")

    def initialize_lives(self, lives=3):
        """
        Initializes the player's lives.
        :param lives: Number of lives to start with.
        """
        self.lives = lives
        print(f"Player starts with {self.lives} lives.")

    def lose_life(self):
        """
        Decreases the player's lives by 1. Ends the game if lives reach 0.
        """
        if self.is_running and self.lives > 0:
            self.lives -= 1
            print(f"Player lost a life! Lives remaining: {self.lives}")
            if self.lives == 0:
                print("No lives remaining. Game over!")
                self.end_game()
        else:
            print("Game is not running or no lives left.")

    def spawn_boss(self):
        """
        Spawns a boss when the player defeats an enemy.
        The boss moves twice as fast as a regular opponent.
        """
        if self.is_running:
            self.opponent = Boss(speed_multiplier=2)
            print("A boss has appeared! It moves twice as fast!")
        else:
            print("Game is not running. Cannot spawn a boss.")

    def display_score_and_lives(self):
        """
        Displays the current score and remaining lives of the player.
        """
        if self.is_running:
            print(f"Score: {self.score}, Lives: {self.lives}")
        else:
            print("Game is not running.")
    