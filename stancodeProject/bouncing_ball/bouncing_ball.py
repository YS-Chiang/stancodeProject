"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Create window and the black ball
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True

# Global variable
# Count the start times of the bouncing ball
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # Add the black ball in the window at the start position
    window.add(ball, x=START_X - SIZE / 2, y=START_Y - SIZE / 2)
    # Execute the bouncing ball
    onmouseclicked(start)


def start(event):
    # The initial velocity of the bouncing ball in the y direction.
    vy = 0
    # Change the constant count to the variable.
    global count
    # Make sure the ball in the start position and the start tome of the bouncing ball is less than 3
    if ball.x == START_X - SIZE / 2 and ball.y == START_Y - SIZE / 2 and count < 3:
        # Make sure the position of the ball in the window
        while ball.x <= window.width:
            # Check the moving direction of the ball
            if ball.y + SIZE/2 < window.height:
                vy = vy + GRAVITY
                ball.move(VX, vy)
                pause(DELAY)
            # Make sure the ball touch the bottom and move to the other direction.
            if ball.y + SIZE/2 >= window.height:
                vy = -vy
                if vy < 0:
                    # The momentum loss of the ball
                    vy = vy * REDUCE
                ball.move(VX, vy)
                pause(DELAY)
        # Put the other ball at the start position
        window.add(ball, x=START_X - SIZE / 2, y=START_Y - SIZE / 2)
        # Count the start times of the bouncing ball
        count += 1






if __name__ == "__main__":
    main()
