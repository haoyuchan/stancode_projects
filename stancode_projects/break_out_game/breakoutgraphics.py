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
BRICK_WIDTH = 40       # Width of a brick (in pixels)
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
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=window_width/2-self.paddle.width/2,
                        y=window_height-paddle_offset-self.paddle.height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball_startpoint_x = window_width//2-ball_radius
        self.ball_startpoint_y = window_height//2-ball_radius
        self.window.add(self.ball, x=window_width//2-ball_radius, y=window_height//2-ball_radius)

        # Draw bricks
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                brick.filled = True
                if 0 <= i < 2:
                    brick_color = "red"
                elif 2 <= i < 4:
                    brick_color = "orange"
                elif 4 <= i < 6:
                    brick_color = "yellow"
                elif 6 <= i < 8:
                    brick_color = "green"
                else:
                    brick_color = "blue"
                brick.fill_color = brick_color
                brick.color = brick_color

                brick.x = (brick.width + BRICK_SPACING) * j
                brick.y = (brick.height + BRICK_SPACING) * i + brick_offset
                self.window.add(brick, x=brick.x, y=brick.y)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)

        # Initialize switch
        self.is_moving = False
        onmouseclicked(self.ball_is_moving)

        # Create a score Label
        self.score = 0
        self.score_label = GLabel("Scores: " + str(self.score))
        self.score_label.font = "-20"
        self.window.add(self.score_label, x=0, y=window_height)

        # Create a win label
        self.win_label = GLabel("You win!!!")
        self.win_label.font = "-40"

        # Create a lose label
        self.lose_label = GLabel("Game over")
        self.lose_label.font = "-40"

        # Create a start label
        self.start_label = GLabel("click to start")
        self.start_label.font = "-40"
        self.window.add(self.start_label, x=window_width/2-self.start_label.width/2,
                        y=window_height/2-self.start_label.height/2)

        # Create a lives label
        self.lives = 0
        self.lives_label = GLabel("lives: " + str(self.lives))
        self.lives_label.font = "-20"
        self.window.add(self.lives_label, x=window_width-self.lives_label.width, y=window_height)

    # Method
    def set_ball_velocity(self):
        if self.is_moving:  # True, set the ball velocity
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def ball_is_moving(self, event):
        self.is_moving = True
        self.window.remove(self.start_label)
        self.set_ball_velocity()

    def move_paddle(self, event):
        if 0 + self.paddle.width/2 <= event.x <= self.window.width - self.paddle.width/2 \
                and 0 <= event.y <= self.window.height:  # mouse event between window
            self.window.add(self.paddle, x=event.x-self.paddle.width/2, y=self.paddle.y)

    def detect_corner_hit(self):
        for i in range(self.ball.x, self.ball.x + self.ball.width + 1, self.ball.width):
            for j in range(self.ball.y, self.ball.y + self.ball.height + 1, self.ball.height):
                maybe_object = self.window.get_object_at(i, j)

                if maybe_object is not None and maybe_object is not self.score_label and \
                        maybe_object is not self.lives_label:

                    # when ball hits the paddle it bounces
                    if maybe_object is self.paddle:
                        if self.__dy > 0:
                            self.__dy = -self.__dy
                        return

                    # when ball hits the brick, remove the brick
                    else:
                        self.window.remove(maybe_object)
                        self.score += 1
                        self.score_label.text = "Scores: " + str(self.score)  # updating the lives label
                        self.__dy = -self.__dy
                        return

    # Getter
    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    # Setter
    def set_vx(self):
        self.__dx = -self.__dx

    def set_vy(self):
        self.__dy = -self.__dy

