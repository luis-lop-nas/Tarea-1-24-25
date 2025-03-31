from Character import Character
import time



class Player(Character):
    def __init__(self, name, score=0, lives=3):
        super().__init__(name)
        self.score = score
        self.lives = lives

    def move(self, direction):
        # Implement movement logic here
        print(f"{self.name} moves {direction}")

    def shoot(self, Projectile):
        """
        Simulates the player shooting a projectile.
        """
        # Create a projectile object (assuming a Projectile class exists)
        projectile = Projectile(self.name, position=self.position, direction="forward")
        print(f"{self.name} shoots a projectile!")
        return projectile

    def collide(self, other_entity):
        # Implement collision logic here
        if hasattr(other_entity, "is_enemy_shot") and other_entity.is_enemy_shot:
            self.lives -= 1
            print(f"{self.name} was hit! Lives remaining: {self.lives}")
            if self.lives <= 0:
                print(f"Game Over for {self.name}!")
        elif hasattr(other_entity, "is_enemy") and other_entity.is_enemy:
            # If the player collides with an enemy, shoot automatically
            print(f"{self.name} collided with an enemy!")
            self.shoot(Projectile)
                
    def reset(self):
        # Reset player-specific attributes
        self.score = 0
        self.lives = 3
        print(f"{self.name} has been reset.")
    
    def serialize(self):
        """
        Serializes the player's state.
        :return: A dictionary representing the player's state.
        """
        data = super().serialize()
        data.update({
            "score": self.score,
            "lives": self.lives
        })
        return data
    def deserialize(self, data):
        """"
        "Deserializes the player's state from a dictionary."
        """
        super().deserialize(data)
        self.score = data["score"]
        self.lives = data["lives"]
    def __str__(self):
        return f"Player {self.name} with score {self.score} and lives {self.lives}"
    

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
    
    