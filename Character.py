from Entity import Entity
from Shoot import Shoot
import pygame

class Character(Entity):
    
    def __init__(self, lives):
        super().__init__()
        self.lives = lives
        
    def move(self, direction):
        
        step = 1  # Define the step size for movement
        if direction == 'up':
            self.y -= step  # Move up by decreasing the y-coordinate
        elif direction == 'down':
            self.y += step  # Move down by increasing the y-coordinate
        elif direction == 'left':
            self.x -= step  # Move left by decreasing the x-coordinate
        elif direction == 'right':
            self.x += step  # Move right by increasing the x-coordinate
        else:
            print(f"Invalid direction: {direction}")

    def shoot(self, direction="up", speed=5):
        """
        Allows the character to shoot in a specified direction with a given speed.
        """
        shoot = Shoot(x=self.x, y=self.y, direction=direction, speed=speed, owner=self)
        return shoot
    
    def collide(self, other_entity):
        """
        Handles collision with another entity.
        """
        if self.is_alive and other_entity.is_alive:
            if hasattr(other_entity, "is_enemy_shot") and other_entity.is_enemy_shot:
                self.lives -= 1
                print(f"Character was hit! Lives remaining: {self.lives}")
                if self.lives <= 0:
                    self.is_alive = False
                    print("Character is dead!")

    def reset(self):
        """
        Resets the character's state.
        """
        self.lives = 3
        self.is_alive = True
        self.x = 0  # Reset position to the origin or a default value
        self.y = 0
        self.bullets = 100  # Reset bullets to a default value
        self.image = None  # Reset image or set to a default value
        print("Character has been reset to its initial state.")

    def __str__(self):
        """
        Returns a string representation of the character.
        """
        return f"Character with {self.lives} lives, alive: {self.is_alive}, position: ({self.x}, {self.y}), image: {self.image}"

    def serialize(self):
        """
        Serializes the character's state into a dictionary.
        """
        return {
            "lives": self.lives,
            "is_alive": self.is_alive,
            "x": self.x,
            "y": self.y,
            "bullets": getattr(self, "bullets", 0),
            "image": self.image
        }

    @classmethod
    def deserialize(cls, data):
        """
        Deserializes the character's state from a dictionary.
        """
        character = cls(lives=data.get("lives", 3))
        character.is_alive = data.get("is_alive", True)
        character.x = data.get("x", 0)
        character.y = data.get("y", 0)
        character.bullets = data.get("bullets", 100)
        character.image = data.get("image", None)
        return character