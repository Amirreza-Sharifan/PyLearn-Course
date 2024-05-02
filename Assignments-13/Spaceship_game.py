import arcade
from spaceship import Spaceship
from enemy import Enemy

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="AmirrezA Spaceship Game")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self.width)
        self.enemy = Enemy(self.width, self.height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        self.enemy.draw()

    def on_key_press(self, symbol: int, modifiers: int):

        if symbol == 65363:
            self.me.center_x = self.me.center_x + self.me.speed

        elif symbol == 65361:
            self.me.center_x = self.me.center_x - self.me.speed

        elif symbol == 65362:
            self.me.center_y = self.me.center_y + self.me.speed

        elif symbol == 65364:
            self.me.center_y = self.me.center_y - self.me.speed

    def on_update(self, delta_time: float):
        self.enemy.center_y = self.enemy.center_y - self.enemy.speed

window = Game()
arcade.run()
