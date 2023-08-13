import pygame
import sys
# todo: keep a circle where the mouse was pressed that shows dx and dy
pygame.init()

screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Circles")
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 2)
player2_pos = pygame.Vector2(screen.get_width() * 3 / 4, screen.get_height() / 2)
player3_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

is_mouse_clicked = False
original_mouse_position = None
max_speed = 300

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                is_mouse_clicked = True
                original_mouse_position = pygame.mouse.get_pos()
                pygame.mouse.set_visible(False)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                is_mouse_clicked = False
                pygame.mouse.set_visible(True)
                pygame.mouse.set_pos(original_mouse_position)

    screen.fill(pygame.Color(122, 255, 122))

    if is_mouse_clicked:
        current_mouse_position = pygame.mouse.get_pos()
        pygame.draw.circle(screen, "white", original_mouse_position, 5)
        delta_x = (current_mouse_position[0] - original_mouse_position[0]) * 5
        delta_y = (current_mouse_position[1] - original_mouse_position[1]) * 5

        if delta_x > 300:
            delta_x = 300
        elif delta_x < -300:
            delta_x = -300
        if delta_y > 300:
            delta_y = 300
        elif delta_y < -300:
            delta_y = -300

        player3_pos = (
            player3_pos[0] + delta_x * dt,
            player3_pos[1] + delta_y * dt
        )


    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.circle(screen, "blue", player2_pos, 20)
    pygame.draw.circle(screen, "black", player3_pos, 60)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    if keys[pygame.K_UP]:
        player2_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player2_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player2_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player2_pos.x += 300 * dt

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()