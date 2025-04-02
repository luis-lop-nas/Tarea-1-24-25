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
        """
        return f"Shot at ({self.x}, {self.y}) with speed {self.speed}, alive: {self.is_alive}, star: {self.is_star}, bomb: {self.is_bomb}"
    
            
    def move(self):
        """
        Moves the shot based on its speed.
        """
        self.y -= self.speed  # Move the shot upwards by reducing its y-coordinate
        if self.y < 0:  # Check if the shot is out of bounds
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
            return True

        return False

    def explode(self):
        """
        Handles the logic for when the shot explodes.
        """
        if self.is_bomb and not self.is_bomb_exploded:
            self.is_bomb_exploded = True
            self.is_alive = False  # The shot is no longer alive after exploding
            # Add additional explosion logic here, such as affecting nearby entities

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

