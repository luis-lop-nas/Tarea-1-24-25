from Entity import Entity
from Shoot import Shoot
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

    def shoot(self):
        """
        Allows the character to shoot.
        """
        shoot = Shoot(self.x, self.y, direction="up", speed=5)
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
