from Character import Character

class Player(Character):
    def __init__(self, name, score = 0, lives = 3):
        super().__init__(name)  
        self.score = score
        self.lives = lives

    def move(self, direction):
        print(f"Moving player {self.name} in direction: {direction}")
    
    def shoot(self):
        print(f"Player {self.name} is shooting!")
        
    