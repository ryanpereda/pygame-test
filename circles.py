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
MAX_DISTANCE = 60
MAX_SPEED = 300
SPEED_DISTANCE_RATIO = 300 / 60
CURSOR_CIRCLE_RADIUS = 5

player_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 2)
player2_pos = pygame.Vector2(screen.get_width() * 3 / 4, screen.get_height() / 2)
player3_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

is_mouse_clicked = False
original_mouse_position = None

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
        delta_x = (current_mouse_position[0] - original_mouse_position[0]) * SPEED_DISTANCE_RATIO
        delta_y = (current_mouse_position[1] - original_mouse_position[1]) * SPEED_DISTANCE_RATIO

        current_mouse_distance = pygame.math.Vector2(
            current_mouse_position[0] - original_mouse_position[0],
            current_mouse_position[1] - original_mouse_position[1]
        ).length()

        if current_mouse_distance > MAX_DISTANCE:
            scale_factor = MAX_DISTANCE / current_mouse_distance
            delta_x *= scale_factor
            delta_y *= scale_factor
            current_mouse_position = (
                int(original_mouse_position[0] + scale_factor * (current_mouse_position[0] - original_mouse_position[0])),
                int(original_mouse_position[1] + scale_factor * (current_mouse_position[1] - original_mouse_position[1]))
            )
            pygame.mouse.set_pos(current_mouse_position)
        
        player3_pos = (
            player3_pos[0] + delta_x * dt,
            player3_pos[1] + delta_y * dt
        )
        
        pygame.draw.circle(screen, "grey", original_mouse_position, MAX_DISTANCE)
        pygame.draw.circle(screen, "white", current_mouse_position, CURSOR_CIRCLE_RADIUS)

    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.circle(screen, "blue", player2_pos, 20)
    pygame.draw.circle(screen, "black", player3_pos, 60)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= MAX_SPEED * dt
    if keys[pygame.K_s]:
        player_pos.y += MAX_SPEED * dt
    if keys[pygame.K_a]:
        player_pos.x -= MAX_SPEED * dt
    if keys[pygame.K_d]:
        player_pos.x += MAX_SPEED * dt

    if keys[pygame.K_UP]:
        player2_pos.y -= MAX_SPEED * dt
    if keys[pygame.K_DOWN]:
        player2_pos.y += MAX_SPEED * dt
    if keys[pygame.K_LEFT]:
        player2_pos.x -= MAX_SPEED * dt
    if keys[pygame.K_RIGHT]:
        player2_pos.x += MAX_SPEED * dt

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()