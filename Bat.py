import pygame
from random import randint

class Bat:
    def __init__(self, x, y, width, height):
        self.bat = pygame.Surface((width, height))
        self.bat.fill((randint(0, 255), randint(0, 255), randint(0, 255))) 
        self.bat_rect = self.bat.get_rect()
        self.bat_rect.centerx = x
        self.bat_rect.centery = y
      
    def move_right(self, n, window):
        if self.bat_rect.right < window.get_width():
            self.bat_rect.centerx += n
    
    def move_left(self, n):
        if self.bat_rect.left > 0:
            self.bat_rect.centerx -= n



    def display(self, window):
        window.blit(self.bat, self.bat_rect)