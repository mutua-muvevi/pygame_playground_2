import pygame
import math

from utils.draw_shapes import Shapes


class Entity:
    def __init__(
            self,
            game,
            crashed,
            entity_type,
            shape,
            screen,
            surface,
            color,
            position,
            speed,
            size,
    ):
        self.game = game
        self.crashed = crashed
        self.entity_type = entity_type
        self.screen = screen

        self.direction = "Left"
        self.position = position
        self.color = color
        self.speed = speed
        self.size = (100, 50)

        self.shape = shape
        self.drawn_shape = Shapes(
            shape,
            position,
            size
        )
        self.surface = surface

    def update(self):
        pass

    def render(self):
        if self.shape == "poly":
            shape = self.drawn_shape.draw_poly(
                self.surface,
                self.color,
                (self.position, (130, 180), (120, 200))
            )

            return shape
