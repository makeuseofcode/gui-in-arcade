import arcade
from arcade.gui import UIManager, UIMessageBox

WIDTH = 800
HEIGHT = 600
PLAYER_SPEED = 25

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Simple Game")
        self.player_x = WIDTH // 2
        self.enemy_x = WIDTH - 50
        self.ui_manager = UIManager()
        self.game_over = False

    def setup(self):
        arcade.set_background_color(arcade.color.WHITE)
        self.ui_manager.enable()  # Enable the UI manager

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.player_x, HEIGHT // 2, 20, arcade.color.BLUE)
        arcade.draw_circle_filled(self.enemy_x, HEIGHT // 2, 20, arcade.color.RED)
        if self.game_over:
            self.ui_manager.draw()

    def update(self, delta_time):
        self.enemy_x += 0.5
        if self.enemy_x >= WIDTH:
            self.show_game_over_screen()
            self.game_over = True
        if self.game_over:
            self.ui_manager.enable()
        else:
            self.ui_manager.disable()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_x -= PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player_x += PLAYER_SPEED

    def show_game_over_screen(self):
        message_box = UIMessageBox(
            width=400,
            height=200,
            message_text="Game Over!"
        )
        self.ui_manager.add(message_box)

game = Game()
game.setup()
arcade.run()
