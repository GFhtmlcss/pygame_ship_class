import pygame
from game_models import *
import sys
import time

# TODO
# 1. надписи в меню
# 2. звуки
# 3. астероид-босс
# 4. анимации
# 5. очки здоровья



class Game:
    pygame.init()
    pygame.display.set_caption('ЗАЩИТНИК ОТ АСТЕРОИДОВ')

    sound_check = 'вкл'

    def __init__(self):
        self.menu()

    def check_collision(self):
        # столкновение корабля с астероидами
        asteroid_collide = pygame.sprite.spritecollide(self.ship, self.asteroids, False)
        for i in asteroid_collide:
            self.ship.ship_check = False
            self.ship.check()
            self.asteroid.kill()

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

            time.sleep(0.7)
            self.dead_menu()

        # пули и астероиды
        bullets_asteroids = pygame.sprite.groupcollide(self.bullets, self.asteroids, True, False)
        for i in bullets_asteroids:
            i.kill()
            bullets_asteroids[i][0].kill()
            self.asteroid.spawn_asteroid()

            self.asteroid_check += 1
            text_text = 'осторожно! астероиды рядом! Твой счет: {}'.format(self.asteroid_check)
            self.text = self.font.render(text_text, True, [240, 160, 75])

        # зеленые пули и астероиды
        bullets_asteroids = pygame.sprite.groupcollide(self.bullets_green, self.asteroids, True, False)
        for i in bullets_asteroids:
            i.kill()
            bullets_asteroids[i][0].kill()
            self.asteroid.spawn_asteroid()

            self.asteroid_check += 1
            text_text = 'осторожно! астероиды рядом! Твой счет: {}'.format(self.asteroid_check)
            self.text = self.font.render(text_text, True, [240, 160, 75])

    def menu(self):
        self.setup_game()

        back_color = 91, 38, 128
        text_color = [255, 255, 64]

        font_m = pygame.font.Font(None, 40)

        text_text_m = 'привет! астероиды рядом! Нажми пробел чтобы защищаться!'
        text_m = font_m.render(text_text_m, True, text_color)
        text_position_m = (self.window_height / 5, 50)

        options_text = 'нажми O, чтобы перейти в настройки'
        text_o = font_m.render(options_text, True, text_color)
        text_position_o = (self.window_height / 2, 150)

        icon = Icon(0, 0)

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.exit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_start()
                    if event.key == pygame.K_o:
                        self.option_menu()

            self.window.fill(back_color)
            self.window.blit(text_m, text_position_m)
            self.window.blit(text_o, text_position_o)
            self.window.blit(icon.image, (0, self.window_height - icon.scale))
            pygame.display.update()

    def option_menu(self):
        fill_color = 31, 125, 99
        text_color = [102, 226, 117]

        font_m = pygame.font.Font(None, 40)

        o_text_text = 'Нажми M, чтобы вернуться в меню'
        o_text = font_m.render(o_text_text, True, text_color)
        text_position_o = (self.window_height / 2, 70)

        sound_text = 'Нажми s, чтобы вкл/выкл звуки в игре. Сейчас звук {}'.format(self.sound_check)
        s_text = font_m.render(sound_text, True, text_color)
        s_position = (self.window_height / 4, 140)

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.exit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.menu()
                    if event.key == pygame.K_s:
                        if self.sound_check == 'вкл':
                            self.sound_check = 'выкл'
                        else:
                            self.sound_check = 'вкл'

                        sound_text = 'Нажми s, чтобы вкл/выкл звуки в игре. Сейчас звук {}'.format(self.sound_check)
                        s_text = font_m.render(sound_text, True, text_color)

            self.window.fill(fill_color)
            self.window.blit(o_text, text_position_o)
            self.window.blit(s_text, s_position)
            pygame.display.update()

    def setup_game(self):
        self.asteroid_check = 0
        self.fire_check = True

        # параметры окна
        self.window_width = 1100
        self.window_height = 600
        self.background = pygame.transform.scale(pygame.image.load('image/bg.jpg'), (self.window_width, self.window_height))
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        self.ship = Ship(self.window_width, self.window_height)

        # текст
        self.font = pygame.font.Font(None, 40)
        self.text_text = 'осторожно! астероиды рядом! Твой счет: {}'.format(self.asteroid_check)
        self.text = self.font.render(self.text_text, True, [240, 160, 75])
        self.text_position = 15, 10

        # группы спрайтов
        self.bullets = pygame.sprite.Group()
        self.bullets_green = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()

        self.asteroid = Asteroid(self.window_width, self.window_height, self.asteroids)

        self.asteroids.add(self.asteroid)

        # fps
        self.clock = pygame.time.Clock()
        self.FPS = 60

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
        text_color = [255, 255, 255]

        font_m = pygame.font.Font(None, 40)
        text_text_m = 'Корабль уничтожен. Счет до уничтожения: {}.'.format(self.asteroid_check)
        text_m = font_m.render(text_text_m, True, text_color)
        text_position_m = self.window_height / 6, 50

        text_new = 'Нажми ПРОБЕЛ, чтобы перейти в меню!'
        text_n = font_m.render(text_new, True, text_color)
        text_position_new = self.window_height / 3, 150

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.exit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.menu()

            self.window.fill(back_color)
            self.window.blit(text_m, text_position_m)
            self.window.blit(text_n, text_position_new)
            pygame.display.update()

    def exit_game(self):
        pygame.quit()
        sys.exit()


game = Game()
