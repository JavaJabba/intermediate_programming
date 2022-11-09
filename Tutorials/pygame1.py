import sys, pygame
pygame.init()

class window():

    size = width, height = 1000, 500
    black = 0, 0, 0

screen = pygame.display.set_mode(size)

class ball:

    def __init__(self, speed:tuple) -> None:
        self.speed = speed
        self.ball = pygame.image.load("intro_ball.gif")
        self.ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ball.ballrect = ball.ballrect.move(ball.speed)
    if ball.ballrect.left < 0 or ball.ballrect.right > window.width:
        ball.speed[0] = -ball.speed[0]
    if ball.ballrect.top < 0 or ball.ballrect.bottom > window.height:
        ball.speed[1] = -ball.speed[1]

    screen.fill(window.black)
    screen.blit(ball.ball, ball.ballrect)
    pygame.display.flip()

ball()
