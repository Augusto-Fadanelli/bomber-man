from abc import ABC, abstractmethod
import numpy as np
import pygame
from pygame.locals import *


class Map(ABC):
    def __init__(self, theme:str):
        self.theme = theme

        # LOAD ASSETS
        self.assets = []
        self.__load_assets()

        self.is_barrier = []

    def __load_assets(self):
        self.assets.append(pygame.image.load(f'assets/{self.theme}/ground.jpg'))
        self.assets.append(pygame.image.load(f'assets/{self.theme}/burnt_ground.jpg'))
        self.assets.append(pygame.image.load(f'assets/{self.theme}/barricade.jpg'))
        self.assets.append(pygame.image.load(f'assets/{self.theme}/box.jpg'))
        self.assets.append(pygame.image.load(f'assets/{self.theme}/side_wall.jpg'))
        self.assets.append(pygame.image.load(f'assets/{self.theme}/vertical_wall.jpg'))

    def set_barriers(self, map:np.matrix):
        self.is_barrier = []
        for line in range(11):
            for column in range(13):
                if map[line, column] == 'BA' or map[line, column] == 'BO':
                    self.is_barrier.append(((column+1), (line+1)))
                    #self.is_barrier.append(((line+1) * 64, (column+1) * 64))
        #debug
        for element in self.is_barrier:
            print(element)

    def get_barriers(self):
        return self.is_barrier

    @abstractmethod
    def generate(self, screen):
        pass

    @abstractmethod
    def get_map(self):
        pass


class Classic(Map):
    def __init__(self, theme:str):
        super().__init__(theme)

        '''
            GR - ground
            BG - burnt ground
            BA - barricade
            BO - box
        '''
        # A matriz deve ser 13x11
        self.__map = np.matrix([['GR', 'GR', 'GR', 'BO', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR', 'GR'],
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

        self.set_barriers(self.__map)

    def generate(self, screen):
        for line in range(13):
            for column in range(15):
                x = (column + 1) * 64
                y = (line + 1) * 64
                if(line < 11 and column < 13):
                    match self.__map[line, column]:
                        case 'GR':
                            screen.blit(self.assets[0], (x, y))
                        case 'BG':
                            screen.blit(self.assets[1], (x, y))
                        case 'BA':
                            screen.blit(self.assets[2], (x, y))
                        case 'BO':
                            screen.blit(self.assets[3], (x, y))
                if(column == 0 or column == 14):
                    screen.blit(self.assets[4], (column * 64, line * 64))
                elif(line == 0 or line == 12):
                    screen.blit(self.assets[5], (column * 64, line * 64))

    def update_map(self, item:str, pos:tuple):
        # item: 'BO' or 'GR' or 'BG'
        # pos >= (0, 0) and pos < (13, 15)
        try:
            self.__map[pos[0], pos[1]] = item
            self.set_barriers(self.__map)
        except:
            print('Error: Map - update_map')

    def check_collision(self, player_pos):
        pass

    def get_map(self):
        return self.__map