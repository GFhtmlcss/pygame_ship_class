import pygame
from game_models import *


class Game(pygame.sprite.Sprite):
    pygame.init()

    ship = Ship()

    # для проверок
    ship_check = True

    # подсчет
    asteroid_check = 0

    window_width = 1100
    window_height = 600
    background = pygame.transform.scale(pygame.image.load('image/bg.jpg'), (window_width, window_height))
    window = pygame.display.set_mode((window_width, window_height))

    # текст
    font = pygame.font.Font(None, 40)
    text_text = 'осторожно! астероиды рядом! Твой счет: {}'.format(asteroid_check)
    text = font.render(text_text, True, [240, 160, 75])
    text_position = 15, 10

    # fps
    clock = pygame.time.Clock()
    FPS = 60

    def _init_(self):
        self.game = Game()

    def game_start(self):

        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
                # if event.type == pygame.KEYDOWN:
                    # if event.key == pygame.K_SPACE:
                        # now = pygame.time.get_ticks()
                        # now_green = pygame.time.get_ticks()
                        # ship.fire()

            self.window.blit(self.background, (0, 0))
            self.window.blit(self.text, self.text_position)
            self.window.blit(self.ship.image, (0, 0))

            self.clock.tick(self.FPS)
            pygame.display.update()

game = Game()
game.game_start()
