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
    lives = NUM_LIVES
    graphics.lives_label.text = "lives: " + str(lives)  # adding lives label
    score = 0
    # Add the animation loop here!
    while True:
        if graphics.is_moving and lives > 0:  # True, when ball is moving and lives > 0
            while True:
                # update
                vx = graphics.get_vx()
                vy = graphics.get_vy()
                graphics.ball.move(vx, vy)
                # check
                # Detect the four points of the ball
                graphics.detect_corner_hit()

                # score >= 100,you win the game
                if score >= 100:
                    graphics.window.add(graphics.win_label, x=graphics.window.width / 2 - graphics.win_label.width / 2,
                                        y=graphics.window.height / 2 - graphics.win_label.height / 2)
                    graphics.window.add(graphics.ball, x=graphics.ball_startpoint_x, y=graphics.ball_startpoint_y)
                    break

                # when ball hits window edge it bounces
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    graphics.set_vx()
                if graphics.ball.y <= 0:
                    graphics.set_vy()

                # when ball hits the window floor, you will lose the life
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    pause(FRAME_RATE)
                    lives -= 1
                    graphics.lives_label.text = "lives: " + str(lives)
                    graphics.is_moving = False
                    break
                pause(FRAME_RATE)

            # resetting ball position
            if score < 100:
                graphics.window.add(graphics.ball, x=graphics.ball_startpoint_x, y=graphics.ball_startpoint_y)

        # when lives == 0 , show the losing label
        if lives == 0:
            graphics.window.add(graphics.lose_label, x=graphics.window.width/2-graphics.lose_label.width/2,
                                y=graphics.window.height/2-graphics.lose_label.height/2)
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
