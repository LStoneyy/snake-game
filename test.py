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
# size is the first argument, needs two parameters!
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

""" To let the game run until you click to exit, we need to establish
    an infinite loop until the exit condition is met. Here, we use
    a while loop for this, due to its simple structure for an infinite loop.
    """

while True:  # starting the infinite loop
    for event in pygame.event.get():  # pygame.event.get() fetches the e
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    """ Uncomment the following to see if you set up everything correctly
        You should see a black window, which you can quit by closing it. """

    # window.fill("black")
    # pygame.display.update()
    # fps_controller.tick(60)

    window.fill("black")
    pygame.display.update()
    fps_controller.tick(60)
