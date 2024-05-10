import arcade
import random
class Enemy(arcade.Sprite):
    def __init__(self, game_width, game_heigh, initial_speed=2):
        super().__init__(":resources:images/space_shooter/playerLife1_orange.png")
        self.center_x = random.randint(0,game_width) 
        self.center_y = game_heigh + 20
        self.angle = 180
        self.width = 40
        self.height = 40
        self.speed = initial_speed

    def move(self):
        self.center_y = self.center_y - self.speed