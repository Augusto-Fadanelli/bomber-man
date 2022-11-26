from abc import ABC, abstractmethod
import pygame


class Character(ABC):
    @abstractmethod
    def get_sprite(self, direction):
        pass

    @abstractmethod
    def get_speed(self):
        pass


class Rodolfo(Character):
    def __init__(self):
        # LOAD SPRITES
        self.__sprites_image = pygame.image.load('assets/sprites/characters/rodolfo.png')
        self.__sprites_image_flipped = pygame.transform.flip(self.__sprites_image, True, False)  # Espelha a imagem
        self.__up_motion = []
        self.__left_motion = []
        self.__down_motion = []
        self.__right_motion = []
        self.__current_sprite = 0 # Contador para os sprites
        self.__is_idle = True
        self.__load_sprites()

        self.__speed = 4  # Velocidade do personagem

    def __load_sprites(self):
        self.__up_motion.append(self.__sprites_image.subsurface((0, 0, 64, 64)))
        self.__up_motion.append(self.__sprites_image.subsurface((512, 0, 64, 64)))
        self.__up_motion.append(self.__sprites_image.subsurface((576, 0, 64, 64)))

        self.__left_motion.append(self.__sprites_image_flipped.subsurface((320, 0, 64, 64)))
        self.__left_motion.append(self.__sprites_image_flipped.subsurface((256, 0, 64, 64)))
        self.__left_motion.append(self.__sprites_image_flipped.subsurface((192, 0, 64, 64)))
        self.__left_motion.append(self.__sprites_image_flipped.subsurface((128, 0, 64, 64)))

        self.__down_motion.append(self.__sprites_image.subsurface((64, 0, 64, 64)))
        self.__down_motion.append(self.__sprites_image.subsurface((128, 0, 64, 64)))
        self.__down_motion.append(self.__sprites_image.subsurface((192, 0, 64, 64)))

        self.__right_motion.append(self.__sprites_image.subsurface((256, 0, 64, 64)))
        self.__right_motion.append(self.__sprites_image.subsurface((320, 0, 64, 64)))
        self.__right_motion.append(self.__sprites_image.subsurface((384, 0, 64, 64)))
        self.__right_motion.append(self.__sprites_image.subsurface((448, 0, 64, 64)))

    def get_sprite(self, direction):
        match direction:

            case 'UP':
                if self.__is_idle:
                    return self.__sprites_image.subsurface((0, 0, 64, 64))

                self.__current_sprite += 0.3
                if self.__current_sprite >= len(self.__up_motion):
                    self.__current_sprite = 0
                return self.__up_motion[int(self.__current_sprite)]

            case 'LEFT':
                if self.__is_idle:
                    return self.__sprites_image_flipped.subsurface((320, 0, 64, 64))

                self.__current_sprite += 0.3
                if self.__current_sprite >= len(self.__left_motion):
                    self.__current_sprite = 0
                return self.__left_motion[int(self.__current_sprite)]

            case 'DOWN':
                if self.__is_idle:
                    return self.__sprites_image.subsurface((64, 0, 64, 64))

                self.__current_sprite += 0.3
                if self.__current_sprite >= len(self.__down_motion):
                    self.__current_sprite = 0
                return self.__down_motion[int(self.__current_sprite)]

            case 'RIGHT':
                if self.__is_idle:
                    return self.__sprites_image.subsurface((256, 0, 64, 64))

                self.__current_sprite += 0.3
                if self.__current_sprite >= len(self.__right_motion):
                    self.__current_sprite = 0
                return self.__right_motion[int(self.__current_sprite)]

    def get_speed(self):
        return self.__speed

    def set_idle(self, is_idle):
        self.__is_idle = is_idle
