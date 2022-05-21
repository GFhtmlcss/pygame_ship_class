import pygame
from game_models import *
import sys


class Game(pygame.sprite.Sprite):
    pygame.init()

    # для проверок


    # подсчет
    asteroid_check = 0


    window_width = 1100
    window_height = 600
    background = pygame.transform.scale(pygame.image.load('image/bg.jpg'), (window_width, window_height))
    window = pygame.display.set_mode((window_width, window_height))

    ship = Ship(window_width, window_height)

    asteroid = Asteroid(window_width, window_height)

    # текст
    font = pygame.font.Font(None, 40)
    text_text = 'осторожно! астероиды рядом! Твой счет: {}'.format(asteroid_check)
    text = font.render(text_text, True, [240, 160, 75])
    text_position = 15, 10

    bullets = pygame.sprite.Group()
    bullets_green = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroids.add(asteroid)

    # fps
    clock = pygame.time.Clock()
    FPS = 60

    def check_collision(self):
        global ship_check
        asteroid_collide = pygame.sprite.spritecollide(self.ship, self.asteroids, False)
        for i in asteroid_collide:
            self.dead_menu()
            ship_check = False
            self.ship.check()
            self.asteroid.kill()

        # пули и астероиды
        bullets_asteroids = pygame.sprite.groupcollide(self.bullets, self.asteroids, True, False)
        for i in bullets_asteroids:
            i.kill()
            bullets_asteroids[i][0].kill()
            self.asteroid.spawn_asteroid(self.asteroids)

            self.asteroid_check += 1
            text_text = 'осторожно! астероиды рядом! Твой счет: {}'.format(self.asteroid_check)
            self.text = self.font.render(text_text, True, [240, 160, 75])

        bullets_asteroids = pygame.sprite.groupcollide(self.bullets_green, self.asteroids, True, False)
        for i in bullets_asteroids:
            i.kill()
            bullets_asteroids[i][0].kill()
            self.asteroid.spawn_asteroid(self.asteroids)

            self.asteroid_check += 1
            text_text = 'осторожно! астероиды рядом! Твой счет: {}'.format(self.asteroid_check)
            self.text = self.font.render(text_text, True, [240, 160, 75])


    def __init__(self):
        self.menu()

    def menu(self):
        back_color = 15, 60, 40

        font_m = pygame.font.Font(None, 40)
        text_text_m = 'привет! астероиды рядом! Нажми пробел чтобы защищаться!'
        text_m = font_m.render(text_text_m, True, [100, 149, 237])
        text_position_m = self.window_height / 6, 50
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.exit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_start()

                    self.window.fill(back_color)
                    self.window.blit(text_m, text_position_m)
                    pygame.display.update()

    def game_start(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.exit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ship.fire(self.bullets, self.bullets_green)

            self.check_collision()

            self.ship.update()
            self.bullets.update()
            self.bullets_green.update()
            self.asteroids.update(self.asteroid)

            self.window.blit(self.background, (0, 0))
            self.bullets.draw(self.window)
            self.bullets_green.draw(self.window)
            self.asteroids.draw(self.window)
            self.window.blit(self.text, self.text_position)
            self.window.blit(self.ship.image, (self.ship.rect.x, self.ship.rect.y))

            self.clock.tick(self.FPS)
            pygame.display.update()

    def dead_menu(self):
        back_color = 0, 0, 0

        font_m = pygame.font.Font(None, 40)
        text_text_m = 'О нет... Счет до уничтожения: {}.'.format(self.asteroid_check)
        text_m = font_m.render(text_text_m, True, [255, 255, 255])
        text_position_m = self.window_height / 6, 50
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.QUIT:
                        self.exit_game()
                    if event.key == pygame.K_SPACE:
                        self.game_start()

                    self.window.fill(back_color)
                    self.window.blit(text_m, text_position_m)
                    pygame.display.update()
    def exit_game(self):
        pygame.quit()
        sys.exit()



game = Game()
game.menu()
