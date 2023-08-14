import pygame
import sys

pygame.init()
running = True

screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("dots?")
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color(255, 255, 255))

    for y in range (48):
        for x in range (48):
            pygame.draw.circle(screen, "blue", (((screen_width * 7 / 8) * (x) / 48) + screen_width / 16, ((screen_height * 7 / 8) * (y) / 48) + screen_height / 16), 5)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()