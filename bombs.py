import pygame


class Bomb():
    def __init__(self):
        # LOAD SPRITES
        self.__sprites_image = pygame.image.load('assets/sprites/bomb.png')
        self.__sprites_bomb = []
        self.__sprites_explosion = []
        self.__sprites_fire = []
        self.__current_sprite = 0  # Contador para os sprites
        self.__load_sprites()

        self.__pos = ()
        self.__explode = False
        self.__update_speed = 0.05

    def __load_sprites(self):
        self.__sprites_bomb.append(self.__sprites_image.subsurface((0, 0, 64, 64)))
        self.__sprites_bomb.append(self.__sprites_image.subsurface((64, 0, 64, 64)))
        self.__sprites_bomb.append(self.__sprites_image.subsurface((128, 0, 64, 64)))
        self.__sprites_bomb.append(self.__sprites_image.subsurface((192, 0, 64, 64)))
        self.__sprites_bomb.append(self.__sprites_image.subsurface((256, 0, 64, 64)))
        self.__sprites_bomb.append(self.__sprites_image.subsurface((320, 0, 64, 64)))

        self.__sprites_explosion.append(self.__sprites_image.subsurface((128, 64, 64, 64)))
        self.__sprites_explosion.append(self.__sprites_image.subsurface((64, 64, 64, 64)))
        self.__sprites_explosion.append(self.__sprites_image.subsurface((0, 64, 64, 64)))
        self.__sprites_explosion.append(self.__sprites_image.subsurface((192, 64, 64, 64)))
        self.__sprites_explosion.append(self.__sprites_image.subsurface((0, 64, 64, 64)))
        self.__sprites_explosion.append(self.__sprites_image.subsurface((64, 64, 64, 64)))
        self.__sprites_explosion.append(self.__sprites_image.subsurface((128, 64, 64, 64)))

    def __update(self):
        self.__current_sprite += self.__update_speed
        if self.__current_sprite >= len(self.__sprites_bomb) and not self.__explode:
            self.__explode = True
            self.__update_speed = 0.3
            self.__current_sprite = 0

    def is_end_of_animation(self):
        if self.__current_sprite >= len(self.__sprites_explosion) and self.__explode:
            print('end')
            return True
        return False

    def get_sprite(self):
        self.__update()
        if self.__explode:
            try:
                return self.__sprites_explosion[int(self.__current_sprite)]
            except:
                return self.__sprites_explosion[0]
        return self.__sprites_bomb[int(self.__current_sprite)]

    def set_pos(self, pos):
        self.__pos = pos

    def get_pos(self):
        return self.__pos
