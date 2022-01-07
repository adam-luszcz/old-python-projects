import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, win, color, width=10, height=100):
        pygame.sprite.Sprite.__init__(self)
        self.win = win
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = 5
        self.score = 0

    def get_player_pos(self):
        return self.rect.x, self.rect.y

    def set_player_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def draw(self, win, pos=tuple()):
        win.blit(self.image, pos)
        pygame.display.update()

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y <= 600 - self.height:
            self.rect.y += self.speed

    def update(self):
        self.movement()
        self.draw(self.win, self.get_player_pos())


class Ball(pygame.sprite.Sprite):
    def __init__(self, win, color, width=10, height=10):
        pygame.sprite.Sprite.__init__(self)
        self.win = win
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = 5
        self.x_speed = -2
        self.y_speed = 3

    def get_ball_pos(self):
        return self.rect.x, self.rect.y

    def set_ball_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def draw(self, win, pos=tuple()):
        win.blit(self.image, pos)
        pygame.display.update()

    def add_force(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        self.change_y()

    def change_y(self):
        if self.rect.y <= 0:
            self.y_speed *= -1
        elif self.rect.y >= 600:
            self.y_speed *= -1

    def change_x(self):
        self.x_speed *= -1

    def check_collision(self, player, ball):
        return pygame.sprite.collide_rect(player, ball)

    # If true player 2 scored, if false player 1 scored
    def scored(self, window_width):
        if self.rect.x < 0:
            return True
        elif self.rect.x > window_width:
            return False

    def update(self):
        self.draw(self.win, self.get_ball_pos())
        self.add_force()


class Player2(Player):
    def __init__(self, win, color):
        Player.__init__(self, win, color)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y <= 600 - self.height:
            self.rect.y += self.speed
