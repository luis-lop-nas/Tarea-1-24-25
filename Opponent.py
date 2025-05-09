from Character import Character
from Shoot import Shoot
import pygame

class Opponent(Character):
    def __init__(self, is_star=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_star = is_star
        
    def __str__(self):
        return f"Opponent with {self.lives} lives and is_star={self.is_star}"

    def move(self):
        """
        Implements the logic for the opponent's movement.
        Opponents move horizontally back and forth across the screen.
        """
        if self.position.x <= 0 or self.position.x >= self.screen_width - self.width:
            self.velocity.x = -self.velocity.x  # Reverse direction when hitting screen edges
        self.position.x += self.velocity.x
        
    def is_opponent(self):
        """
        Returns True if the entity is an opponent.
        :return: True if the entity is an opponent, False otherwise.
        """
        return True

    def shoot(self):
        """
        Implements the logic for the opponent's shooting.
        Opponents shoot bullets at regular intervals or based on specific conditions.
        """
        if self.is_alive:
            bullet_position = self.position.copy()
            bullet_position.y += self.height  # Start the bullet just below the opponent
            bullet_velocity = self.velocity.copy()
            bullet_velocity.x = 0  # Bullets move straight down
            bullet_velocity.y = 5  # Set the bullet's downward speed
            
            return Shoot(position=bullet_position, velocity=bullet_velocity, owner=self)
        return None
    
    def collide(self, other_entity):
        """
        Handles collision with another entity.
        :param other_entity: The entity this opponent collides with.
        """
        if other_entity.type == "player_bullet":
            self.is_alive = False
            other_entity.owner.score += 1  # Increment the player's score
        pass
    
    def reset(self):
        """"
        "Resets the opponent's state.
        """
        self.lives = 3
        self.is_alive = True
        # Reset other opponent-specific attributes here
        pass
    
    def serialize(self):
        """
        Serializes the opponent's state into a dictionary.
        """
        return {
            "is_star": self.is_star,
            "lives": self.lives,
            "is_alive": self.is_alive,
            "position": {"x": self.position.x, "y": self.position.y},
            "velocity": {"x": self.velocity.x, "y": self.velocity.y},
        }

    @classmethod
    def deserialize(cls, data, *args, **kwargs):
        """
        Deserializes a dictionary into an Opponent object.
        :param data: The dictionary containing the opponent's state.
        """
        opponent = cls(is_star=data["is_star"], *args, **kwargs)
        opponent.lives = data["lives"]
        opponent.is_alive = data["is_alive"]
        opponent.position.x = data["position"]["x"]
        opponent.position.y = data["position"]["y"]
        opponent.velocity.x = data["velocity"]["x"]
        opponent.velocity.y = data["velocity"]["y"]
        return opponent