"""This is a simple Snake-Clone made entirely in Python using the PyGame
Library. The code is meant to be as simple as possible so that
the game can be used as a selfstudy course for pupils of technology
in German classrooms."""

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
window = pygame.display.set_mode(window_size_x, window_size_y)
pygame.display.set_caption("Snake Game - Python")

""" To control the output Frames per Second, we need to
    initialise a clock controller."""
fps_controller = pygame.time.Clock()

""" To display colors, we need to define them first, using RGB values. """
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
