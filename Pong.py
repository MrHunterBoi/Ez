import pygame
import ctypes
from paddle import Paddle
from ball import Ball

pygame.init()
White = (255,255,255)
Black = (0,0,0)
user32 = ctypes.windll.user32
size = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddle1 = Paddle(White,10,100)
paddle1.rect.x = user32.GetSystemMetrics(78)/18
paddle1.rect.y = 200
paddle2 = Paddle(White,10,100)
paddle2.rect.x = user32.GetSystemMetrics(78)/18*17
paddle2.rect.y = 200
ball = Ball(White,10,10)
ball.rect.x = 345
ball.rect.y = 195	

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle1)
all_sprites_list.add(paddle2)
all_sprites_list.add(ball)

Cycle = True
clock = pygame.time.Clock()

score1 = 0
score2 = 0
while Cycle:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Cycle = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				Cycle = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		paddle1.moveUp(5)
	if keys[pygame.K_s]:
		paddle1.moveDown(5)
	if keys[pygame.K_UP]:
		paddle2.moveUp(5)
	if keys[pygame.K_DOWN]:
		paddle2.moveDown(5)
	all_sprites_list.update()
	if ball.rect.x>=user32.GetSystemMetrics(78):
		score1 += 1
		ball.velocity[0] = -ball.velocity[0]
	if ball.rect.x<=0:
		ball.velocity[0] = -ball.velocity[0]
		score2 += 1
	if ball.rect.y>user32.GetSystemMetrics(79):
		ball.velocity[1] = -ball.velocity[1]
	if ball.rect.y<0:
		ball.velocity[1] = -ball.velocity[1]
	if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
		ball.bounce()
	screen.fill(Black)
	pygame.draw.line(screen,White,[user32.GetSystemMetrics(78)/2,0],[user32.GetSystemMetrics(78)/2,user32.GetSystemMetrics(79)],5)
	all_sprites_list.draw(screen)

	font = pygame.font.Font(None,74)
	text = font.render(str(score1),1,White)
	screen.blit(text,(user32.GetSystemMetrics(78)/3,10))
	text = font.render(str(score2),1,White)
	screen.blit(text,(user32.GetSystemMetrics(78)/3*2,10))
	pygame.display.flip()
	clock.tick(60)
pygame.quit()