from Player import Player
from Opponent import Opponent
from Boss import Boss


class game:
    def __init__(self):
        self.player = None
        self.enemy = None
        self.turn = None
        self.game_over = False
        self.score = 0  # Atributo para registrar la puntuación

    def start_game(self, Player, Enemy):
        print("Welcome to the game!")
        self.player = Player()
        self.enemy = Enemy()
        self.turn = "player"
        self.game_over = False
        self.score = 0  # Reinicia la puntuación al inicio del juego

    def update_score(self, points):
        """
        Actualiza la puntuación del jugador.
        :param points: Número de puntos a añadir o restar.
        """
        self.score += points
        print(f"Score updated! Current score: {self.score}")

    def play_turn(self):
        if self.turn == "player":
            self.player.take_turn(self.enemy)
            if self.enemy.health <= 0:
                print("You defeated the enemy!")
                self.update_score(100)  # Añade puntos al derrotar al enemigo
                self.game_over = True
            else:
                self.turn = "enemy"
        else:
            self.enemy.take_turn(self.player)
            if self.player.health <= 0:
                print("You were defeated by the enemy!")
                self.update_score(-50)  # Resta puntos si el jugador pierde
                self.game_over = True
            else:
                self.turn = "player"

    def end_game(self):
        print(f"Game over! Final score: {self.score}")  # Muestra la puntuación final
        print("Thanks for playing.")
        self.game_over = True

    def run(self):
        self.start_game()
        while not self.game_over:
            self.play_turn()
        self.end_game()
