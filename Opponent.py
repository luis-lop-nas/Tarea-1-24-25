from Character import Character

class Opponent(Character):
    def __init__(self, is_star=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_star = is_star

    def move(self):
        # Implement the logic for the opponent's movement
        pass

    def shoot(self):
        # Implement the logic for the opponent's shooting
        pass
    def collide(self, other_entity):
        """
        Handles collision with another entity.
        :param other_entity: The entity this opponent collides with.
        """
        if other_entity.type == "player_bullet":
            self.is_alive = False
            other_entity.owner.score += 1  # Increment the player's score
        pass
    def reset(self):
        """"
        "Resets the opponent's state.
        """
        self.lives = 3
        self.is_alive = True
        # Reset other opponent-specific attributes here
        pass
    def serialize(self):
        """"
        "Serializes the opponent's state."
        "     :return: A dictionary representing the opponent's state.
        """
        data = super().serialize()
        data.update({
            "is_star": self.is_star
        })
        return data
    def deserialize(self, data):
        """"
        "Deserializes the opponent's state from a dictionary."
        """
        super().deserialize(data)
        self.is_star = data["is_star"]
    def __str__(self):
        return f"Opponent with {self.lives} lives and is_star={self.is_star}"
    