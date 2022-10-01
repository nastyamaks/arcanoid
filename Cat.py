import pygame
from math import sin, cos, radians

class Cat:
    def __init__(self, x, y, speed, direction):
        self.cat_is_shout = pygame.image.load("cat_in_arcanoid.png")
        self.cat_is_shout_rect = self.cat_is_shout.get_rect()
        self.cat_is_shout_rect.centerx = x
        self.cat_is_shout_rect.centery = y

        self.speed = speed
        self.direction = direction

        self.brick_sound = pygame.mixer.Sound('louds/brick.wav')
        self.bottom_sound = pygame.mixer.Sound('louds/bottom.wav')
        self.bat_sound = pygame.mixer.Sound('louds/bat.wav')
        self.walls_sound = pygame.mixer.Sound('louds/walls.wav')


    def move(self, window):
        self.cat_is_shout_rect.centerx += cos(radians(self.direction)) * self.speed
        self.cat_is_shout_rect.centery += sin(radians(self.direction)) * self.speed

        self.check_wall_collision(window)
        
  
    def check_wall_collision(self, window):
        if self.cat_is_shout_rect.top < 0:
            self.direction = -self.direction
            self.cat_is_shout_rect.top = 0
            self.walls_sound.play()
        if self.cat_is_shout_rect.right > window.get_width():
            self.direction = 180 - self.direction
            self.cat_is_shout_rect.right = window.get_width()
            self.walls_sound.play()
        if self.cat_is_shout_rect.left < 0:
            self.direction = 180 - self.direction
            self.cat_is_shout_rect.left = 0
            self.walls_sound.play()

    def check_bottom_collision(self, window):
        if self.cat_is_shout_rect.bottom > window.get_height(): 
            self.bottom_sound.play()
            return True
        return False    


    def check_bat_collision(self, bat):
        if (self.cat_is_shout_rect.bottom > bat.bat_rect.top) and (self.cat_is_shout_rect.right > bat.bat_rect.left) and \
            (self.cat_is_shout_rect.left < bat.bat_rect.right):
            self.direction = -self.direction
            self.cat_is_shout_rect.bottom = bat.bat_rect.top
            self.bat_sound.play()
            return True
        return False

    
    def check_bricks_collision(self, bricks):
        for brick in bricks:
            if (self.cat_is_shout_rect.bottom > brick.brick_rect.top) and (self.cat_is_shout_rect.right > brick.brick_rect.left) and \
                (self.cat_is_shout_rect.left < brick.brick_rect.right) and (self.cat_is_shout_rect.top < brick.brick_rect.bottom):
                self.direction = -self.direction
                bricks.remove(brick)
                self.brick_sound.play()
                return True

        return False


    def display(self, window):
        window.blit(self.cat_is_shout, self.cat_is_shout_rect)
