
from text_input import TextInput
import pygame
from Cat import Cat
from Bat import Bat
from Brick import create_row_of_bricks
from random import randint
from Records import Records

STATUS_GAME = 0
STATUS_GAME_OVER = 1
STATUS_RECORDS = 2

class Game:

    def __init__(self, window):
        self.records = Records()
        self.init_game(window)
        
    def init_game(self, window):
        self.cat_1 = Cat(400, 300, 3, self.generate_direction())
        
        self.bat = Bat(window.get_width()// 2, 550, 200, 30)
        self.add_bricks(window)
        self.score_font = pygame.font.SysFont('Kristen ITC', 100)
        self.font = pygame.font.SysFont('Kristen ITC', 50)
        self.textinput = TextInput()
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        

        pygame.key.set_repeat(18)

        self.score = 0
        self.status = STATUS_GAME

    def generate_direction(self):
        direction = randint(-135, -45)
        while direction > -105 and direction < -75:
            direction = randint(-135, -45)
        return direction

    def add_bricks(self, window):
        self.bricks = create_row_of_bricks(60, 30, 20, window.get_width() - 20, 50, 10)
        self.bricks += create_row_of_bricks(60, 30, 50, window.get_width() - 50, 100, 10)
        self.bricks += create_row_of_bricks(60, 30, 80, window.get_width() - 80, 150, 1)

    def play(self, window, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.bat.move_left(10)
                if event.key == pygame.K_RIGHT:
                    self.bat.move_right(10, window)
            
        self.cat_1.move(window)
        

        
        if (self.cat_1.check_bottom_collision(window)):
            pygame.key.set_repeat()
            self.status = STATUS_GAME_OVER

        if (self.cat_1.check_bricks_collision(self.bricks)):
            self.score += 1

        if self.cat_1.check_bat_collision(self.bat) and len(self.bricks) == 0:
            self.add_bricks(window)
            
        window.fill(self.color)
        self.cat_1.display(window)
        
        self.bat.display(window)
        
        for brick in self.bricks:
            brick.display(window)

        score_text = self.score_font.render(str(self.score), True, (0, 0, 0))
        window.blit(score_text, (300, 50))

    def game_over(self, window, events):
        
        window.fill((255, 255, 230))

        again = self.font.render("GAME OVER.", True, (0, 0, 0))
        again_0 = self.font.render("Your score is " + str(self.score),  True, (0, 0, 0))
        again_1 = self.font.render("Please enter your name", True, (0, 0, 0))
        window.blit(again, (190, 180))
        window.blit(again_0, (190, 250))
        window.blit(again_1, (190, 320))
        
        if self.textinput.update(events) and self.textinput.get_text() != '':
            name = self.textinput.get_text()
            self.records.add(name, self.score)
            self.status = STATUS_RECORDS


        window.blit(self.textinput.get_surface(), (10, 10))

    def show_records(self, window, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.init_game(window)
        window.fill((255, 255, 230))
        self.records.display(window)
        Enter = self.font.render("Press enter to start new game", True, (0, 0, 0))
        window.blit(Enter, (30, 500))

    def display(self, window, events):
        if self.status == STATUS_GAME:
            self.play(window, events)
        elif self.status == STATUS_GAME_OVER:
            self.game_over(window, events)
        elif self.status == STATUS_RECORDS:
            self.show_records(window, events)      