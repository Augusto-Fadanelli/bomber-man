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
        self.__sprites_image_flipped = pygame.transform.flip(self.__sprites_image, True, False) # Espelha a imagem

        self.__speed = 5 # Velocidade do personagem
        self.__pos = (50, 50) # Posição do personagem
        self.__direction = None # Informa a direção que o personagem deve se movimentar
        self.__is_flipped = False # Indica se a imagem está espelhada ou não

    def get_sprite(self):
        if self.__is_flipped:
            return self.__sprites_image_flipped
        return self.__sprites_image

    def get_cropped_image(self, mode, loop_index:int):
        match mode:
            case 'FRONT_IDLE':
                self.__is_flipped = False
                return (64, 0, 64, 64)
            case 'BACK_IDLE':
                self.__is_flipped = False
                return (0, 0, 64, 64)
            case 'LEFT_IDLE':
                self.__is_flipped = True
                return (320, 0, 64, 64)
            case 'RIGHT_IDLE':
                self.__is_flipped = False
                return (256, 0, 64, 64)
            case 'UP_RUN':
                pass
            case 'DOWN_RUN':
                pass
            case 'LEFT_RUN':
                pass
            case 'RIGHT_RUN':
                pass

    def move(self): 
        match self.__direction:
            case 'UP': 
                self.__pos = (self.__pos[0], self.__pos[1] - self.__speed)
            case 'DOWN':
                self.__pos = (self.__pos[0], self.__pos[1] + self.__speed)
            case 'LEFT':
                self.__pos = (self.__pos[0] - self.__speed, self.__pos[1])
            case 'RIGHT':
                self.__pos = (self.__pos[0] + self.__speed, self.__pos[1])

    def stop_move(self):
        self.__direction = None

    def set_direction(self, direction):
        self.__direction = direction

    def get_pos(self):
        return self.__pos

#    def set_pos(self):
        
    def get_speed(self):
        return self.__speed



