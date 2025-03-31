from Entity import Entity

class Shot(Entity):

    def __init__(self, x, y, image, speed):
        """
        Initializes a Shot object.
        :param x: The x-coordinate of the shot.
        :param y: The y-coordinate of the shot.
        :param image: The image representing the shot.
        :param speed: The speed of the shot.
        """
        super().__init__(x, y, image)
        self.speed = speed
        self.is_alive = True
        self.is_star = False
        self.is_bomb = False
        self.is_bomb_exploded = False

    def __str__(self):
        """
        Returns a string representation of the shot.
        :return: A string representing the shot's state.
        """
        return f"Shot at ({self.x}, {self.y}) with speed {self.speed}, alive: {self.is_alive}, star: {self.is_star}, bomb: {self.is_bomb}"
    
            
    def move(self):
        # Implement logic to move the shot
        pass

    def hit_target(self):
        # Implement logic to check if the shot hits a target
        pass

    def explode(self):
        # Implement logic for explosion
        pass

    def reset(self):
        """
        Resets the shot's state.
        """
        self.is_alive = True
        self.is_star = False
        self.is_bomb = False
        self.is_bomb_exploded = False
        # Reset other shot-specific attributes here
        self.x = 0
        self.y = 0
        self.speed = 0

    def serialize(self):
        """
        Serializes the shot's state.
        :return: A dictionary representing the shot's state.
        """
        data = super().serialize()
        data.update({
            "speed": self.speed,
            "is_alive": self.is_alive,
            "is_star": self.is_star,
            "is_bomb": self.is_bomb,
            "is_bomb_exploded": self.is_bomb_exploded
        })
        return data
    def deserialize(self, data):
        """"
        "Deserializes the shot's state from a dictionary."
        """
        super().deserialize(data)
        self.speed = data["speed"]
        self.is_alive = data["is_alive"]
        self.is_star = data["is_star"]
        self.is_bomb = data["is_bomb"]
        self.is_bomb_exploded = data["is_bomb_exploded"]

    