"""This is a simple Snake-Clone made entirely in Python using the PyGame
Library. The code is meant to be as simple as possible so that
the game can be used as a selfstudy course for pupils of technology
in German classrooms. It is based on the PyGame Documentation, which
can be consulted on https://www.pygame.org/docs/"""

# We first need to import the used modules, including PyGame
import pygame
import random
import sys

""" We first need to create a window where our game will be rendered.
    We use the x- and y-axis to define the width and height of
    our window in pixels."""
window_size_x = 720
window_size_y = 480

""" We now need to initialise a window. For this, we initialise PyGame,
    set a display with the mode of our intended window size and set
    a caption. """
pygame.init()
window = pygame.display.set_mode((window_size_x, window_size_y))
pygame.display.set_caption("Snake Game - Python")

# at this point, if you run the file, a window should appear

""" To control the output Frames per Second, we need to
    initialise a clock controller."""
fps_controller = pygame.time.Clock()

""" To display colors, we need to define them first, using RGB values.
    These are defined in a String using the PyGame Color class. """
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

""" To create the snake, we use a list. In order to display the snake,
    we need to know its length, its position and its size. In a
    multidimensional list, these values can be stored, updated and
    changed accordingly. """
snake_position = [50, 50]
snake_length = [[50, 50], [40, 50], [30, 50]]

""" We also need to define the direction the snake is going.
    We use a default value ("RIGHT") and a variable (direction_change)
    to store the changed values. """
direction = "RIGHT"
direction_change = direction

""" We also need to spawn food on the screen. This is done
    using a random function to position it within the window bounds."""
food_position = [random.randrange(1, window_size_x // 10) * 10,
                 random.randrange(1, window_size_y // 10) * 10]
food_spawn = True

""" Lastly, we need a score that can be displayed somewhere. This is
    a simple Integer. """
score = 0

""" To let the game run until you click to exit, we need to establish
    an infinite loop until the exit condition is met. Here, we use
    a while loop for this, due to its simple structure for an infinite loop.
    """

while True:  # The game runs indefinitely until an exit condition is met
    for event in pygame.event.get():  # Checking all events
        if event.type == pygame.QUIT:  # If the window is closed
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # If a key is pressed
            # The snake cannot reverse direction immediately to prevent self-collision
            if event.key == pygame.K_UP and direction != "DOWN":
                direction_change = "UP"
            if event.key == pygame.K_DOWN and direction != "UP":
                direction_change = "DOWN"
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction_change = "LEFT"
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction_change = "RIGHT"

    """ After processing the input, we update the snake's direction.
        This ensures the snake moves in the intended direction, if valid. """
    direction = direction_change

    """ The position of the snake's head is now updated.
        Depending on the direction, either the x- or y-coordinate is adjusted. """
    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10

    """ The snake eats food if the head's position matches the food's position.
        In this case, we increase the score and do not remove the last element,
        making the snake longer. """
    snake_length.insert(0, list(snake_position))
    if snake_position == food_position:
        score += 1
        food_spawn = False
    else:
        snake_length.pop()

    """ If food has been eaten, generate a new random food position within bounds. """
    if not food_spawn:
        food_position = [random.randrange(1, window_size_x // 10) * 10,
                         random.randrange(1, window_size_y // 10) * 10]
    food_spawn = True

    """ Now, we need to redraw the background to avoid visual artifacts
        and then update the snake's new position. """
    window.fill(black)
    for segment in snake_length:
        pygame.draw.rect(window, green, pygame.Rect(segment[0], segment[1], 10, 10))

    """ Draw the food as a red rectangle on the screen at its position. """
    pygame.draw.rect(window, red, pygame.Rect(food_position[0], food_position[1], 10, 10))

    """ If the snake hits the boundary or collides with itself, the game ends. """
    if (snake_position[0] < 0 or snake_position[0] >= window_size_x or
        snake_position[1] < 0 or snake_position[1] >= window_size_y):
        break

    for segment in snake_length[1:]:
        if snake_position == segment:
            break

    """ Finally, the window is updated, and the frame rate is controlled
        to ensure the game does not run too fast or too slow. """
    pygame.display.update()
    fps_controller.tick(10)

""" If the game loop is exited due to a collision, we display 'Game Over', as well
as the final score. """
window.fill(black)
font = pygame.font.SysFont("times new roman", 50)
font_2 = pygame.font.SysFont("times new roman", 30) 
game_over_text = font.render("Game Over", True, red)
score_text = font_2.render("Your score: "+ str(score), True, white)
game_over_rect = game_over_text.get_rect(center=(window_size_x // 2, window_size_y // 2))
score_text_rect = score_text.get_rect(center=(window_size_x // 2, window_size_y // 1.5))
window.blit(game_over_text, game_over_rect)
window.blit(score_text, score_text_rect)
pygame.display.update()
pygame.time.delay(3000)
pygame.quit()
sys.exit()
