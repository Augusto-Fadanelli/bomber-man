from abc import ABC, abstractmethod
import pygame
from pygame.locals import *


class Character(ABC):
    pass


class Rodolfo(Character):
    pass


class Player:
    def __init__(self, character):
        self.character = character
        
        # LOAD SPRITES
        self.__sprites_image = pygame.image.load(f'assets/sprites/characters/{self.character}.png')

    def get_sprite(self):
        return self.__sprites_image

    def get_cropped_image(self, mode, loop_index:int):
        match mode:
            case 'FRONT_IDLE':
                return (64, 0, 64, 64)
            case 'BACK_IDLE':
                return (0, 0, 64, 64)
            case 'LEFT_IDLE':
                pass
            case 'RIGHT_IDLE':
                return (256, 0, 64, 64)
            case 'UP_RUN':
                pass
            case 'DOWN_RUN':
                pass
            case 'LEFT_RUN':
                pass
            case 'RIGHT_RUN':
                pass



