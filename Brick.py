import pygame
from random import randint


class Brick:
    def __init__(self, x, y, width, height, colour):
        self.brick = pygame.Surface((width, height))
        self.brick.fill(colour) 
        self.brick_rect = self.brick.get_rect()
        self.brick_rect.centerx = x
        self.brick_rect.centery = y

    def display(self, window):
        window.blit(self.brick, self.brick_rect)


def create_row_of_bricks(width, height, x_start, x_end, y, distance):
    bricks = []
    for x in range(x_start + width // 2, x_end, width + distance):
        bricks.append(Brick(x, y, width, height, (randint(0, 255), randint(0, 255), randint(0, 255))))
    return bricks