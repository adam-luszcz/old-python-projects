import pygame
import Objects


class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH = 800
        self.HEIGHT = 600
        self.COLOR_WHITE = (255, 255, 255)
        self.COLOR_BLACK = pygame.image.load("bg.png")
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pong")
        self.make_players()
        self.make_ball()
        self.FONT = pygame.font.SysFont("Monospace", 50)

    def make_players(self):
        self.player = Objects.Player(self.WINDOW, self.COLOR_WHITE)
        self.player.set_player_pos(30, (self.HEIGHT - self.player.height) // 2)

        self.player2 = Objects.Player2(self.WINDOW, self.COLOR_WHITE)
        self.player2.set_player_pos(self.WIDTH - 30, (self.HEIGHT - self.player2.height) // 2)

    def make_ball(self):
        self.ball = Objects.Ball(self.WINDOW, self.COLOR_WHITE)
        self.ball.set_ball_pos(self.WIDTH // 2, self.HEIGHT // 2)

    def check_collisions(self, player1, player2, ball):
        if pygame.sprite.collide_rect(player1, ball) or pygame.sprite.collide_rect(ball, player2):
            ball.change_x()

    def scored(self):
        # Player 2 scored
        if self.ball.scored(self.WIDTH):
            self.player2.score += 1
            self.make_ball()
        # Player 1 scored
        elif self.ball.scored(self.WIDTH) == False:
            self.player.score += 1
            self.make_ball()
            self.ball.change_x()

    def font_handling(self, font, pos):
        self.UI_SCORES = font.render(f"{self.player.score}   {self.player2.score}", 1, self.COLOR_WHITE)
        self.WINDOW.blit(self.UI_SCORES, (pos[0], pos[1]))

    def update(self):
        self.WINDOW.blit(self.COLOR_BLACK, (0, 0))
        self.player.update()
        self.player2.update()
        self.ball.update()
        self.scored()
        self.check_collisions(self.player, self.player2, self.ball)
        self.font_handling(self.FONT, (self.WIDTH // 2 - 70, 50))
        pygame.display.update()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.update()
            self.clock.tick(144)

    def change_resolution(self, w, h):
        self.WINDOW = pygame.display.set_mode((w, h))


game = Game()
game.run()
