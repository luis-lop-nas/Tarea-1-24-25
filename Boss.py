from Opponent import Opponent

class Boss(Opponent):
    def __init__(self, x, y, speed):
        # Llama al constructor de la clase base Opponent
        super().__init__(x, y, speed * 2)  # El jefe final se mueve el doble de rápido

    def special_attack(self):
        # Implementa un ataque especial del jefe final
        print("El jefe final realiza un ataque especial devastador.")
        # Lógica adicional para el ataque especial
        damage = 50  # Daño del ataque especial
        print(f"El ataque especial causa {damage} puntos de daño.")
        return damage

    def reset(self):
        # Resetea el estado del jefe final
        super().reset()
        print("El jefe final ha sido reseteado.")
        
    def serialize(self):
        """"
        "Deserializa el estado del jefe final desde un diccionario."
        """
        data = super().serialize()
        data.update({
            "special_attack": self.special_attack
        })
        return data
    
    def deserialize(self, data):
        """"
        "Deserializa el estado del jefe final desde un diccionario."
        """
        super().deserialize(data)
        self.special_attack = data["special_attack"]

    def __str__(self):
        """
        Devuelve una representación en cadena del jefe final.
        :return: Una cadena que representa el estado del jefe final.
        """
        return f"Jefe Final en ({self.x}, {self.y}) con velocidad {self.speed}"
    
    def move(self):
        # Implementa la lógica de movimiento del jefe final
        print(f"El jefe final se mueve a ({self.x}, {self.y})")
        
    def hit_target(self):
        # Implementa la lógica para verificar si el jefe final golpea un objetivo
        print("El jefe final ha golpeado un objetivo.")