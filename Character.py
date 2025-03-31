from Entity import Entity

class Character(Entity):
    def __init__(self, lives):
        super().__init__()
        self.lives = lives
        
    def move(self, direction):
        """
        Moves the character in the specified direction.
        :param direction: A string indicating the direction (e.g., 'up', 'down', 'left', 'right').
        """
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
        # Implement shooting logic here
        pass

    def collide(self, other_entity):
        """
        Handles collision with another entity.
        :param other_entity: The entity this character collides with.
        """
        # Implement collision logic here
        pass

    def reset(self):
        """
        Resets the character's state.
        """
        self.lives = 3
        self.is_alive = True
        # Reset other character-specific attributes here
        pass

    def __str__(self):
        """
        Returns a string representation of the character.
        :return: A string representing the character's state.
        """
        return f"Character with {self.lives} lives, alive: {self.is_alive}, position: ({self.x}, {self.y}), image: {self.image}"
