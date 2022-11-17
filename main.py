import pygame
from pygame.locals import *
from sys import exit
import numpy as np


class StartGame:
    def __init__(self, map:np.matrix):
        self.map = map

        self.__screen_width = 640
        self.__screen_height = 480
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
        print(self.map)


if __name__ == '__main__': 
    map = np.matrix([[1, 2], [3, 4]])

    pygame.init()
    start = StartGame(map)



