from Entity import Entity

class Shot(Entity):

    def __init__(self, x, y, image, speed, damage, shooter_type):
        """
        Initializes a Shot object.
        :param x: The x-coordinate of the shot.
        :param y: The y-coordinate of the shot.
        :param image: The image representing the shot.
        :param speed: The speed of the shot.
        :param damage: The damage of the shot.
        :param shooter_type: The type of the shooter (player, opponent, boss).
        """
        super().__init__(x, y, image)
        self.speed = speed
        self.damage = damage
        self.shooter_type = shooter_type
        self.is_alive = True
        self.is_star = False
        self.is_bomb = False
        self.is_bomb_exploded = False

        # Set speed and damage based on shooter type
        if shooter_type == "player":
            self.speed = 7
            self.damage = 20
        elif shooter_type == "opponent":
            self.speed = 10
            self.damage = 15
        elif shooter_type == "boss":
            self.speed = 15
            self.damage = 50

    def __str__(self):
        """
        Returns a string representation of the shot.
        """
        return (f"Shot at ({self.x}, {self.y}) with speed {self.speed}, "
                f"damage {self.damage}, alive: {self.is_alive}, "
                f"shooter: {self.shooter_type}, star: {self.is_star}, bomb: {self.is_bomb}")
    
    def move(self):
        """
        Moves the shot based on its speed.
        """
        if self.shooter_type == "player":
            self.y -= self.speed  # Player shots move upwards
        else:
            self.y += self.speed  # Opponent and boss shots move downwards

        if self.y < 0 or self.y > 800:  # Check if the shot is out of bounds (example screen height: 800)
            self.is_alive = False

    def hit_target(self, target):
        """
        Checks if the shot hits a target.
        """
        if not self.is_alive:
            return False  # Dead shots cannot hit targets

        # Check for collision with the target
        if (self.x < target.x + target.width and
            self.x + self.width > target.x and
            self.y < target.y + target.height and
            self.y + self.height > target.y):
            self.is_alive = False  # Mark the shot as not alive after hitting
            target.take_damage(self.damage)  # Apply damage to the target
            return True

        return False

    def reset(self):
        """
        Resets the shot's state.
        """
        self.is_alive = True
        self.is_star = False
        self.is_bomb = False
        self.is_bomb_exploded = False
        self.x = 0
        self.y = 0
        self.speed = 0
        self.damage = 0
        self.shooter_type = None

    def serialize(self):
        """
        Serializes the shot's state into a dictionary.
        """
        return {
            'x': self.x,
            'y': self.y,
            'speed': self.speed,
            'damage': self.damage,
            'shooter_type': self.shooter_type,
            'is_alive': self.is_alive,
            'is_star': self.is_star,
            'is_bomb': self.is_bomb,
            'is_bomb_exploded': self.is_bomb_exploded
        }

    @classmethod
    def deserialize(cls, data):
        """
        Deserializes a dictionary into a Shot object.
        :param data: A dictionary containing the shot's state.
        :return: A Shot object.
        """
        shot = cls(data['x'], data['y'], None, data['speed'], data['damage'], data['shooter_type'])
        shot.is_alive = data['is_alive']
        shot.is_star = data['is_star']
        shot.is_bomb = data['is_bomb']
        shot.is_bomb_exploded = data['is_bomb_exploded']
        return shot
