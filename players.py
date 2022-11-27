from chars import Character
from bombs import *


class Player:
    def __init__(self, character:Character):
        self.character = character

        self.__is_alive = True
        self.__pos = (64, 64) # Posição do personagem
        self.__direction = 'DOWN' # Informa a direção que o personagem deve se movimentar
        self.__is_in_motion = False # Informa se o personagem está em movimento
        self.__is_flipped = False # Indica se a imagem está espelhada ou não

        self.__simple_bombs = []
        self.total_bombs = 3
        self.available_bombs = self.total_bombs
        self.__instantiate_bombs()

    def __instantiate_bombs(self):
        #for bomb in range(self.total_bombs):
        new_bomb = Bomb()
        self.__simple_bombs.append(new_bomb)

    def get_char_sprite(self):
        return self.character.get_sprite(self.__direction)

    def get_bomb_sprite(self, bomb_number):
        return self.__simple_bombs[bomb_number].get_sprite()

    def move(self, is_barrier):
        #debug
        # print(self.__pos)
        # print((self.__pos[0] + 32) // 64, self.__pos[1] // 64)
        if self.__is_in_motion:
            match self.__direction:
                case 'UP':
                    if self.__pos[1] >= 64 + self.character.get_speed(): # Impede de ultrapassar a parede superior
                        if not ((self.__pos[0] + 32) // 64, self.__pos[1] // 64) in is_barrier:
                            self.__pos = (self.__pos[0], self.__pos[1] - self.character.get_speed())
                case 'DOWN':
                    if self.__pos[1] <= 704 - self.character.get_speed(): # Impede de ultrapassar a parede inferior
                        if not ((self.__pos[0] + 32) // 64, (self.__pos[1] + 64) // 64) in is_barrier:
                            self.__pos = (self.__pos[0], self.__pos[1] + self.character.get_speed())
                case 'LEFT':
                    if self.__pos[0] >= 64 + self.character.get_speed(): # Impede de ultrapassar a parede da esquerda
                        if not (self.__pos[0] // 64, (self.__pos[1] + 32) // 64) in is_barrier:
                            self.__pos = (self.__pos[0] - self.character.get_speed(), self.__pos[1])
                case 'RIGHT':
                    if self.__pos[0] <= 832 - self.character.get_speed(): # Impede de ultrapassar a parede da direita
                        if not ((self.__pos[0] + 64) // 64, (self.__pos[1] + 32) // 64) in is_barrier:
                            self.__pos = (self.__pos[0] + self.character.get_speed(), self.__pos[1])

    def stop_move(self):
        self.__is_in_motion = False
        self.character.set_idle(True)

    def set_direction(self, direction):
        self.__direction = direction
        self.__is_in_motion = True
        self.character.set_idle(False)

    def get_pos(self):
        return self.__pos

    def add_bomb(self):
        if self.available_bombs > 0:
            self.available_bombs -= 1
            self.__instantiate_bombs()
            self.__simple_bombs[self.total_bombs - self.available_bombs -1].set_pos(self.__pos)

    def get_bomb_pos(self, bomb_number:int):
        return self.__simple_bombs[bomb_number].get_pos()

    def update_bomb(self, bomb_number): # Verifica se a animação da bomba foi finalizada
        if self.__simple_bombs[bomb_number].is_end_of_animation():
            self.__simple_bombs.pop(bomb_number)
            self.available_bombs += 1
