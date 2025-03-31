from Entity import Entity

class Shot(Entity):
    def __init__(self, x, y, image, speed):
        super().__init__(x, y, image)
        self.speed = speed
        self.is_alive = True
        self.is_start = False
        self

    def move(self):
        """
        Move the shot in the specified direction.
        """
        # Implement movement logic here
        pass

    def collide(self, other_entity, damage):
        self.lives -= damage
        if self.lives <= 0:
            self.is_alive = False
        print(f"Shot collided with {other_entity}.")