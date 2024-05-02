import arcade
class Spaceship(arcade.Sprite):
    def __init__(self, game_width):  
        super().__init__(":resources:images/space_shooter/playerLife1_green.png")
        self.center_x = game_width / 2 
        self.center_y = 80
        self.width = 60
        self.height = 60
        self.speed = 20