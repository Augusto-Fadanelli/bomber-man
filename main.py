import pygame
from pygame.locals import *
from sys import exit
import numpy as np

from players import *


class StartGame:
    def __init__(self, map:np.matrix, theme:str, player:Player):
        self.map = map
        self.theme = theme
        self.player = player

        self.__screen_width = 960
        self.__screen_height = 832
        self.__screen = pygame.display.set_mode((self.__screen_width, self.__screen_height))

        self.__clock = pygame.time.Clock()

        pygame.display.set_caption('Bomber-Man')

        # LOAD ASSETS
        self.__assets = []
        self.__load_assets()

        self.player_direction = 'FRONT_IDLE'

        self.__loop()

    def __loop(self):
        while True:
            self.__clock.tick(60)
            self.__screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_w:
                        self.player_direction = 'BACK_IDLE'
                    elif event.key == K_s:
                        self.player_direction = 'FRONT_IDLE'
                    elif event.key == K_a:
                        self.player_direction = 'LEFT_IDLE'
                    elif event.key == K_d:
                        self.player_direction = 'RIGHT_IDLE'

            self.__map_generate()
            self.__draw_players(self.player_direction)

            pygame.display.update()

    def __map_generate(self):
        for line in range(13):
            for column in range(15):
                x = (column + 1) * 64
                y = (line + 1) * 64
                if(line < 11 and column < 13):
                    match self.map[line, column]:
                        case 'GR':
                            self.__screen.blit(self.__assets[0], (x, y))
                        case 'BG':
                            self.__screen.blit(self.__assets[1], (x, y))
                        case 'BA':
                            self.__screen.blit(self.__assets[2], (x, y))
                        case 'BO':
                            self.__screen.blit(self.__assets[3], (x, y))
                if(column == 0 or column == 14):
                    self.__screen.blit(self.__assets[4], (column * 64, line * 64))
                elif(line == 0 or line == 12):
                    self.__screen.blit(self.__assets[5], (column * 64, line * 64))


    def __load_assets(self):
        self.__assets.append(pygame.image.load(f'assets/{self.theme}/ground.jpg'))
        self.__assets.append(pygame.image.load(f'assets/{self.theme}/burnt_ground.jpg'))
        self.__assets.append(pygame.image.load(f'assets/{self.theme}/barricade.jpg'))
        self.__assets.append(pygame.image.load(f'assets/{self.theme}/box.jpg'))
        self.__assets.append(pygame.image.load(f'assets/{self.theme}/side_wall.jpg'))
        self.__assets.append(pygame.image.load(f'assets/{self.theme}/vertical_wall.jpg'))

    def __draw_players(self, direction:str):
        self.__screen.blit(self.player.get_sprite(), (50, 50), self.player.get_cropped_image(direction, 0))


if __name__ == '__main__':
    '''
    GR - ground
    BG - burnt ground
    BA - barricade
    BO - box
    '''
    # A matriz deve ser 13x11
    map = np.matrix([['GR', 'GR', 'GR', 'BO', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR'], 
                     ['GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR'],
                     ['GR', 'GR', 'BO', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR'], 
                     ['GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR'],
                     ['GR', 'GR', 'GR', 'GR', 'GR', 'BO', 'BO', 'BO', 'GR', 'GR', 'GR', 'GR', 'GR'], 
                     ['GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR'],
                     ['GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR'], 
                     ['GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR'],
                     ['GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR'], 
                     ['GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR', 'BA', 'GR'],
                     ['BO', 'BG', 'BG', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR']])

    player1 = Player('rodolfo');

    pygame.init()
    start = StartGame(map, theme='classic', player=player1)

