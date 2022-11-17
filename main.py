import pygame
from pygame.locals import *
from sys import exit
import numpy as np


class StartGame:
    def __init__(self, map:np.matrix):
        self.map = map

        self.__screen_width = 600
        self.__screen_height = 400
        self.__screen = pygame.display.set_mode((self.__screen_width, self.__screen_height))

        self.__clock = pygame.time.Clock()

        pygame.display.set_caption('Bomber-Man')

        self.__map_generate()
        self.__loop()

    def __loop(self):
        while True:
            self.__clock.tick(60)
            self.__screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            pygame.display.update()

    def __map_generate(self):
        for line in range(4):
            for column in range(6):
                print(self.map[line, column])
                match self.map[line, column]:
                    case 1:
                        print('red')
                    case 2:
                        print('green')
                    case 3:
                        print('blue')
                    case 4:
                        print('yellow')


if __name__ == '__main__': 
    map = np.matrix([[1, 2, 3, 4, 1, 2], 
                     [4, 3, 2, 1, 2, 3],
                     [2, 1, 3, 4, 3, 1],
                     [3, 2, 1, 2, 4, 3]])

    pygame.init()
    start = StartGame(map)



