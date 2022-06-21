"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window.width-self.paddle.width)/2,
                        self.window.height-PADDLE_OFFSET-self.paddle.height)

        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2)
        self.ball.filled = True
        self.window.add(self.ball, self.window.width/2 - BALL_RADIUS, self.window.height/2 - BALL_RADIUS)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        onmouseclicked(self.move_ball)

        # Initialize our mouse listeners
        onmousemoved(self.handle_move)

        # Draw bricks
        self.del_bricks = 0
        self.total = BRICK_ROWS * BRICK_COLS
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.bricks = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.bricks.filled = True
                if i < 2:
                    self.bricks.fill_color = 'red'
                elif i < 4:
                    self.bricks.fill_color = 'yellow'
                elif i < 6:
                    self.bricks.fill_color = 'orange'
                elif i < 8:
                    self.bricks.fill_color = 'green'
                else:
                    self.bricks.fill_color = 'blue'
                self.window.add(self.bricks, 0 + j * (BRICK_WIDTH + BRICK_SPACING),
                                BRICK_OFFSET + i * (BRICK_HEIGHT + BRICK_SPACING))

    # Reset the ball position
    def set_ball_position(self):
        self.ball.x = self.window.width/2 - BALL_RADIUS
        self.ball.y = self.window.height/2 - BALL_RADIUS
        self.__dx = 0
        self.__dy = 0
        onmouseclicked(self.move_ball)

    # Make the paddle move with mouse
    def handle_move(self, event):
        if event.x <= self.paddle.width/2:
            self.paddle.x = 0
        elif event.x >= self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width/2

    # Set the initial velocity of the ball
    def move_ball(self, event):
        if self.__dx == 0 and self.__dy == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    # Return the delta x of the moving ball
    def get_vx(self):
        return self.__dx

    # Return the delta y of the moving ball
    def get_vy(self):
        return self.__dy

    # Make the ball move to the opposite side in x direction
    def set_vx(self):
        self.__dx *= -1

    # Make the ball move to the opposite side in the y direction
    def set_vy(self):
        self.__dy *= -1

    # When the ball contacts the paddle, make the ball move to the opposite side in the y direction
    def check_paddle(self):
        if self.window.get_object_at(self.ball.x, self.ball.y) == self.paddle and self.ball.y > self.paddle.y:
            self.set_vy()
        elif self.window.get_object_at(self.ball.x + 2*BALL_RADIUS, self.ball.y) == self.paddle and \
                self.ball.y > self.paddle.y:
            self.set_vy()
        elif self.window.get_object_at(self.ball.x + 2*BALL_RADIUS, self.ball.y + 2*BALL_RADIUS) == self.paddle and \
                self.ball.y > self.paddle.y:
            self.set_vy()
        elif self.window.get_object_at(self.ball.x, self.ball.y + 2*BALL_RADIUS) == self.paddle and \
                self.ball.y > self.paddle.y:
            self.set_vy()
        else:
            pass

    # When the ball contacts the brick, remove the brick and move to the opposite side in the y direction
    def check_bricks(self):
        ball_lt = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_rt = self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y)
        ball_rb = self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS)
        ball_lb = self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS)
        if ball_lt is not None and ball_lt is not self.paddle:
            self.window.remove(ball_lt)
            self.set_vy()
            self.del_bricks += 1
        elif ball_rt is not None and ball_rt is not self.paddle:
            self.window.remove(ball_rt)
            self.set_vy()
            self.del_bricks += 1
        elif ball_rb is not None and ball_rb is not self.paddle:
            self.window.remove(ball_rb)
            self.set_vy()
            self.del_bricks += 1
        elif ball_lb is not None and ball_lb is not self.paddle:
            self.window.remove(ball_lb)
            self.set_vy()
            self.del_bricks += 1
        else:
            pass

    # Remove all the bricks in the window (Win)
    def win_game(self):
        board_w = GLabel('You win!!! :)')
        board_w.font = '-40'
        self.window.add(board_w, self.window.width/2 - board_w.width/2, self.window.height/2 + board_w.height/2)

    # When the number of lives is 0 (Lose)
    def lose_game(self):
        board_l = GLabel('You lose. :(')
        board_l.font = '-40'
        self.window.add(board_l, self.window.width / 2 - board_l.width / 2, self.window.height / 2 + board_l.height / 2)



