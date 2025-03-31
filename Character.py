from Entity import Entity

class Character(Entity):
    def __init__(self, lives):
        super().__init__()
        self.lives = lives
        self.is_alive = lives > 0

    def move(self, direction):
        """
        Moves the character in the specified direction.
        :param direction: A string indicating the direction (e.g., 'up', 'down', 'left', 'right').
        """
        # Implement movement logic here
        pass

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

    def serialize(self):
        """
        Serializes the character's state.
        :return: A dictionary representing the character's state.
        """
        data = super().serialize()
        data.update({
            "lives": self.lives,
            "is_alive": self.is_alive
        })
        return data
    def deserialize(self, data):
        """"
        "Deserializes the character's state from a dictionary."
        """
        super().deserialize(data)
        self.lives = data["lives"]
        self.is_alive = data["is_alive"]
    def __str__(self):
        """
        Returns a string representation of the character.
        :return: A string representing the character's state.
        """
        return f"Character with {self.lives} lives, alive: {self.is_alive}, position: ({self.x}, {self.y}), image: {self.image}"
    def __eq__(self, other):
        """
        Checks if two characters are equal.
        :param other: The other character to compare with.
        :return: True if the characters are equal, False otherwise.
        """
        return super().__eq__(other) and self.lives == other.lives and self.is_alive == other.is_alive