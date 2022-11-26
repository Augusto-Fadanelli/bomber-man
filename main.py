import pygame
from pygame.locals import *
from sys import exit
import numpy as np

from chars import *
from maps import *
from players import *


class StartGame:
    def __init__(self, map:Map, player:Player):
        self.map = map
        self.player = player

        self.__screen_width = 960
        self.__screen_height = 832
        self.__screen = pygame.display.set_mode((self.__screen_width, self.__screen_height))

        self.__clock = pygame.time.Clock()

        pygame.display.set_caption('Bomber-Man')

        self.__is_keydown = [] # Verifica se as teclas w, a, s, d (respectivamente) estão sendo pressionadas

        self.__loop()

    def __loop(self):
        while True:
            self.__clock.tick(60)
            self.__screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                self.__player_movement(event)

            self.player.move(self.map.get_barriers())

            self.__map_generate()
            self.__draw_players()

            pygame.display.update()

    def __player_movement(self, event):
        # Movimentação do player
        if event.type == KEYDOWN:
            if event.key == K_w:
                self.__is_keydown.append('UP')
            if event.key == K_a:
                self.__is_keydown.append('LEFT')
            if event.key == K_s:
                self.__is_keydown.append('DOWN')
            if event.key == K_d:
                self.__is_keydown.append('RIGHT')
            if event.key == K_k:
                self.map.update_map('BO', (10, 10))
                self.map.update_map('BO', (2, 4))
                self.map.update_map('BO', (5, 1))
                self.map.update_map('BO', (9, 11))

        # Mantém a movimentação mais fluida
        if event.type == KEYUP:
            if event.key == K_w:
                self.__is_keydown.remove('UP')
            if event.key == K_a:
                self.__is_keydown.remove('LEFT')
            if event.key == K_s:
                self.__is_keydown.remove('DOWN')
            if event.key == K_d:
                self.__is_keydown.remove('RIGHT')
            if event.key == K_k:
                self.map.update_map('BG', (10, 10))
                self.map.update_map('BG', (2, 4))
                self.map.update_map('BG', (5, 1))
                self.map.update_map('BG', (9, 11))

        if len(self.__is_keydown) == 0:
            self.player.stop_move()
        else:
            self.player.set_direction(self.__is_keydown[-1])

    def __map_generate(self):
        self.map.generate(self.__screen)

    def __draw_players(self):
        self.__screen.blit(self.player.get_char_sprite(), self.player.get_pos())


if __name__ == '__main__':

    map = Classic('green_prairie')

    char1 = Rodolfo()
    player1 = Player(char1);

    pygame.init()
    start = StartGame(map, player=player1)

