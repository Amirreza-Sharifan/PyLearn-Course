import arcade

class Window(arcade.Window):
    def __init__(self):
        super().__init__(width=550, height=600, title="Complex Loops - Box")
        arcade.set_background_color(arcade.color.WHITE)
        self.diamond_size = 20  
        self.diamond_spacing = 25  

    def on_draw(self):
        arcade.start_render()
        for row in range(15):  
            for col in range(15): 
                x = 100 + col * self.diamond_spacing
                y = 100 + row * self.diamond_spacing
                color = arcade.color.RED if (row + col) % 2 == 0 else arcade.color.BLUE
                arcade.draw_polygon_filled([
                    (x, y + self.diamond_size / 2),
                    (x + self.diamond_size / 2, y),
                    (x, y - self.diamond_size / 2),
                    (x - self.diamond_size / 2, y)
                ], color)

window = Window()
arcade.run()