from Game import Game
import pygame

if __name__ == "__main__":
    game = Game()
    game.start()
    game.update()
    game.end_game()
    game.reset()