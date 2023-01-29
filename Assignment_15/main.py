
import arcade
from fruit import Apple
from fruit import Pear
from fruit import Poop
from snake import Snake


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake 🐍")
        arcade.set_background_color(arcade.color.KHAKI)
        self.apple = Apple(self)
        self.pear = Pear(self)
        self.poop = Poop(self)
        self.snake = Snake(self)
        self.state = 1

    def on_draw(self):
        arcade.start_render()
        self.apple.draw()
        self.pear.draw()
        self.poop.draw()
        self.snake.draw()

        arcade.draw_text(f"Score: {self.snake.score}", 0.02*self.width, 0.02*self.height, arcade.color.BLACK)

        if self.state == 0: 
            arcade.draw_lrtb_rectangle_filled(0,self.width,self.height,0,arcade.color.BLACK)
            arcade.draw_text("GAME OVER!", self.width//6 , self.height//2 , arcade.color.WHITE, 40)

        arcade.finish_render()

    def on_update(self, delta_time):
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.apple):
            del self.apple
            self.snake.score += 1
            self.apple = Apple(self)
        elif arcade.check_for_collision(self.snake, self.pear):
            del self.pear
            self.snake.score += 2
            self.pear = Pear(self)
        elif arcade.check_for_collision(self.snake, self.poop):
            del self.poop
            self.snake.score -= 1
            self.poop = Poop(self)

            if self.snake.score == 0 or self.snake.score < 0:
                self.state = 0
            
        if self.snake.center_x < 0 or self.snake.center_x > 500 or self.snake.center_y < 0 or self.snake.center_y > self.height:
            self.state = 0

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        

if __name__ == "__main__":
    game = Game()
    arcade.run()
    