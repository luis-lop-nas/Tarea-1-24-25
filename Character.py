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
        if hasattr(self, 'bullets') and self.bullets > 0:
            self.bullets -= 1
            print("Character shoots! Bullets left:", self.bullets)
            # Create and return a projectile object or trigger shooting logic
            return {"x": self.x, "y": self.y, "direction": "forward"}  # Example projectile data
        else:
            print("No bullets left to shoot!")
            return None

    def collide(self, other_entity):
        """
        Handles collision with another entity.
        :param other_entity: The entity this character collides with.
        """
        if self.x == other_entity.x and self.y == other_entity.y:
            if hasattr(other_entity, 'damage'):
                self.lives -= other_entity.damage
                print(f"Collision detected! Character takes {other_entity.damage} damage. Lives left: {self.lives}")
                if self.lives <= 0:
                    self.is_alive = False
                    print("Character has died.")
            else:
                print("Collision detected, but no damage attribute found on the other entity.")
        pass

    def reset(self):
        """
        Resets the character's state.
        """
        self.lives = 3
        self.is_alive = True
        self.x = 0  # Reset position to the origin or a default value
        self.y = 0
        self.bullets = 10  # Reset bullets to a default value
        self.image = None  # Reset image or set to a default value
        print("Character has been reset to its initial state.")

    def __str__(self):
        """
        Returns a string representation of the character.
        :return: A string representing the character's state.
        """
        return f"Character with {self.lives} lives, alive: {self.is_alive}, position: ({self.x}, {self.y}), image: {self.image}"
