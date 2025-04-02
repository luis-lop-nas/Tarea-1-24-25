from Opponent import Opponent

class Boss(Opponent):
    
    def __init__(self, x, y, speed):
        # Llama al constructor de la clase base Opponent
        super().__init__(x, y, speed * 1,5)  # El jefe final se mueve más rápido
        
    def __str__(self):
            """
            Devuelve una representación en cadena del jefe final.
            :return: Una cadena que representa el estado del jefe final.
            """
            return f"Jefe Final en ({self.x}, {self.y}) con velocidad {self.speed}"
        
    def move(self):
        # Implementa la lógica de movimiento del jefe final
        print(f"El jefe final se mueve a ({self.x}, {self.y})")    
        
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

    def hit_target(self):
        # Implementa la lógica para verificar si el jefe final golpea un objetivo
        print("El jefe final ha golpeado un objetivo.")
        
    def take_damage(self, damage):
        # Implementa la lógica para recibir daño
        print(f"El jefe final ha recibio {damage} puntos de daño.")
        self.health -= damage
        if self.health <= 0:
            self.derrotado()
    
    def derrotado(self):
        # Implementa la lógica para cuando el jefe final es derrotado
        print("El jefe final ha sido derrotado.")
        self.is_alive = False
        
    def is_boss(self):
        # Verifica si el objeto es un jefe final
        return True
    
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed * 1.5)  # El jefe final se mueve más rápido
        self.enemigos_derrotados = 0  # Contador de enemigos derrotados

    def derrotar_enemigo(self):
        # Implementa la lógica para derrotar a un enemigo
        self.enemigos_derrotados += 1
        print(f"Enemigo abatido. Total derrotados: {self.enemigos_derrotados}")
        if self.enemigos_derrotados >= 3:
            self.spawnear_boss()

    def spawnear_boss(self):
        # Lógica para spawnear el jefe final
        boss = Boss(self.x, self.y, self.speed)
        boss.is_boss = True
        print("¡El jefe final ha aparecido!")
        
    def serialize(self):
        """
        Serializa el estado del jefe final en un diccionario.
        :return: Un diccionario que representa el estado del jefe final.
        """
        return {
            "x": self.x,
            "y": self.y,
            "speed": self.speed,
            "health": self.health,
            "is_alive": self.is_alive,
            "enemigos_derrotados": self.enemigos_derrotados
        }

    @staticmethod
    def deserialize(data):
        """
        Deserializa un diccionario para crear una instancia de Boss.
        :param data: Un diccionario que contiene el estado del jefe final.
        :return: Una instancia de Boss.
        """
        boss = Boss(data["x"], data["y"], data["speed"] / 1.5)  # Ajusta la velocidad al valor original
        boss.health = data["health"]
        boss.is_alive = data["is_alive"]
        boss.enemigos_derrotados = data["enemigos_derrotados"]
        return boss