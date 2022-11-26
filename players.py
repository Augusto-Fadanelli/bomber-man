from chars import Character


class Player:
    def __init__(self, character:Character):
        self.character = character

        self.__is_alive = True
        self.__pos = (64, 64) # Posição do personagem
        self.__direction = 'DOWN' # Informa a direção que o personagem deve se movimentar
        self.__is_in_motion = False # Informa se o personagem está em movimento
        self.__is_flipped = False # Indica se a imagem está espelhada ou não

    def get_char_sprite(self):
        return self.character.get_sprite(self.__direction)

    def move(self, is_barrier):
        #debug
        print(self.__pos)
        print((self.__pos[0] + 32) // 64, self.__pos[1] // 64)
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
