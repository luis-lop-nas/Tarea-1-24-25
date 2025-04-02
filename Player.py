from Character import Character
from Shoot import Shoot
import time

class Player(Character):
    
    def __init__(self, name, score=0, lives=3):
        super().__init__(name)
        self.score = score
        self.lives = lives
        
    def __str__(self):
        return f"Player {self.name} with score {self.score} and lives {self.lives}"

    def move(self, direction):
        """
        Moves the player in the specified direction.
        :param direction: A string indicating the direction ('up', 'down', 'left', 'right').
        """
        valid_directions = ["up", "down", "left", "right"]
        
        if direction not in valid_directions:
            print(f"Invalid direction: {direction}. Valid directions are: {valid_directions}")
            return

        if direction == "up":
            self.position[1] += 1
        elif direction == "down":
            self.position[1] -= 1
        elif direction == "left":
            self.position[0] -= 1
        elif direction == "right":
            self.position[0] += 1

        print(f"{self.name} moves {direction} to position {self.position}")

    def shoot(self):
    
        # Create a projectile object (assuming a Projectile class exists)
        
       shoot = shoot(self.name, is_enemy_shoot=False)
       print(f"{self.name} shoots a projectile!")
       return shoot

    def collide(self, other_entity):
        # Implement collision logic here
        if hasattr(other_entity, "is_enemy_shot") and other_entity.is_enemy_shot:
            self.lives -= 1
            print(f"{self.name} was hit! Lives remaining: {self.lives}")
            if self.lives <= 0:
                self.is_alive = False
                print(f"{self.name} is dead!")
            elif hasattr(other_entity, "is_star") and other_entity.is_star:
                self.score += 10
                print(f"{self.name} collected a star! Score: {self.score}")
            elif hasattr(other_entity, "is_bomb") and other_entity.is_bomb:
                self.lives -= 1
                print(f"{self.name} hit a bomb! Lives remaining: {self.lives}")
                if self.lives <= 0:
                    self.is_alive = False
                    print(f"Game Over {self.name}")
                
    def reset(self):
        # Reset player-specific attributes
        self.score = 0
        self.lives = 3
        print(f"{self.name} has been reset.")
    
    def respawn(self):
        """
        Respawns the player after being hit, if lives remain.
        """
        if self.lives > 0:
            print(f"{self.name} is respawning...")
            time.sleep(2)  # Simulate a brief delay for respawning
            print(f"{self.name} has respawned!")
        else:
            print(f"{self.name} cannot respawn. No lives remaining.")
    
    