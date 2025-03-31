from Opponent import Opponent

class Boss(Opponent):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.special_attack_power = 2 * attack_power

    def special_attack(self):
        print(f"{self.name} uses a special attack with power {self.special_attack_power}!")
        return self.special_attack_power
    
    def __str__(self):
        return f"Boss {self.name} with health {self.health} and attack power {self.attack_power}"
    
    def draw(self):
        print(f"Drawing boss {self.name} at ({self.x}, {self.y}) with image {self.image}")
        