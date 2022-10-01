import pygame

from Game import Game

pygame.init()

window = pygame.display.set_mode((800, 600))

pygame.mixer.music.load('louds/music.mp3')
pygame.mixer.music.set_volume(0.09)

exit_game = False

clock = pygame.time.Clock()


pygame.mixer.music.play()

game = Game(window)

while  not exit_game:
    clock.tick(120)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            exit_game = True

    game.display(window, events)
    pygame.display.flip()
    