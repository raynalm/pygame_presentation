import pygame
import random

SIZE = WIDTH, HEIGHT = 640, 480
BLACK = 0, 0, 0


class Ball(pygame.sprite.Sprite):

    def __init__(self, red=False):
        super().__init__()
        if red:
            self.image = pygame.image.load("ball_red.gif").convert_alpha()
        else:
            self.image = pygame.image.load("ball.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.radius = self.rect.width / 2
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.speed = [random.choice([-1, 1]) * random.randint(1, 3),
                      random.choice([-1, 1]) * random.randint(1, 3)]
        self.explode_sound = pygame.mixer.Sound('balloon_pop.wav')

    def update(self):
        self.rect.move_ip(self.speed)
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed[1] = -self.speed[1]

    def explode(self):
        self.explode_sound.play()


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    red_ball = Ball(red=True)
    yellow_balls = pygame.sprite.RenderPlain([Ball() for _ in range(10)])
    all_sprites = pygame.sprite.RenderPlain((red_ball, yellow_balls))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()
        for ball in pygame.sprite.spritecollide(red_ball, yellow_balls, dokill=1,
                                                collided=pygame.sprite.collide_circle):
            ball.explode()
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.update()
        clock.tick(100)


if __name__ == "__main__":
    main()
