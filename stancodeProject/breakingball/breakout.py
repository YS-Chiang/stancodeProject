"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    global NUM_LIVES
    # Make the ball move
    vx = graphics.get_vx()
    vy = graphics.get_vy()
    graphics.ball.move(vx, vy)
    # Add the animation loop here!
    while True:
        vx = graphics.get_vx()
        vy = graphics.get_vy()
        graphics.ball.move(vx, vy)

        # Check boundary
        if graphics.ball.x < 0 or graphics.ball.x > graphics.window.width - graphics.ball.width:
            graphics.set_vx()
        if graphics.ball.y < 0:
            graphics.set_vy()
        # The ball drops, lose one live
        if graphics.ball.y > graphics.window.height - graphics.ball.height:
            NUM_LIVES -= 1
            # Reset the position of the ball in the start point
            if NUM_LIVES > 0:
                graphics.set_ball_position()
        # When you win or lose the game, break the loop.
        if graphics.del_bricks == graphics.total or NUM_LIVES == 0:
            break
        graphics.check_paddle()
        graphics.check_bricks()
        pause(FRAME_RATE)
    if graphics.del_bricks == graphics.total:
        graphics.win_game()
    if NUM_LIVES == 0:
        graphics.lose_game()


if __name__ == '__main__':
    main()
