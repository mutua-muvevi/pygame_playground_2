import pygame


class Shapes:
    def __init__(self, shape, position, size):
        self.shape = shape
        self.position = list(position)
        self.size = list(size)
        self.drawn_shape = None

    def draw_rect(self, surface, color):
        self.drawn_shape = pygame.draw.rect(
            surface,
            color,
            pygame.Rect(
                self.position[0],
                self.position[1],
                self.size[0],
                self.size[1],
            )
        )

        return self.drawn_shape

    def draw_poly(self, surface, color, points):
        self.drawn_shape = pygame.draw.polygon(
            surface,
            color,
            points
        )

        return self.drawn_shape

    def draw_circle(self, surface, color, center, radius):
        self.drawn_shape = pygame.draw.circle(
            surface,
            color,
            center,
            radius
        )

        return self.drawn_shape
