import pygame
import math

pygame.init()

screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Transformacje 11-kąta')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_polygon(surface, color, n, radius, position, angle_offset=0, vertical_scale=1, horizontal_scale=1,
                 vertical_shear=0, horizontal_shear=0, flip_vertical=False, flip_horizontal=False):
    theta = (2 * math.pi) / n
    points = []
    for i in range(n):
        angle = theta * i + angle_offset
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        x += vertical_shear * y
        y += horizontal_shear * x

        x *= horizontal_scale
        y *= vertical_scale

        if flip_horizontal:
            x *= -1
        if flip_vertical:
            y *= -1

        x += position[0]
        y += position[1]

        points.append((x, y))

    pygame.draw.polygon(surface, color, points)


run = True
angle_offset = 0
vertical_scale = 1
horizontal_scale = 1
vertical_shear = 0
horizontal_shear = 0
flip_vertical = False
flip_horizontal = False
position_offset = (0, 0)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:  # Normalny 11-kąt
        angle_offset = 0
        vertical_scale = 1
        horizontal_scale = 1
        vertical_shear = 0
        horizontal_shear = 0
        flip_vertical = False
        flip_horizontal = False
        position_offset = (0, 0)
    elif keys[pygame.K_2]:  # Obrót 45 stopni
        angle_offset = math.pi / 4
    elif keys[pygame.K_3]:  # Obrót 90 stopni
        angle_offset = math.pi / 2
    elif keys[pygame.K_4]:  # Ścinanie w poziomie
        horizontal_shear = 0.5
    elif keys[pygame.K_5]:  # Skalowanie w poziomie
        horizontal_scale = 1.5
        vertical_scale = 0.5
    elif keys[pygame.K_6]:  # Ścinanie w pionie
        vertical_shear = 0.5
    elif keys[pygame.K_7]:  # Odbicie lustrzane w pionie
        flip_vertical = True
    elif keys[pygame.K_8]:  # Obrót i przesunięcie
        angle_offset = -math.pi / 4
        position_offset = (-30, 180)
    elif keys[pygame.K_9]:  # Odbicie lustrzane w obu osiach
        flip_vertical = True
        flip_horizontal = True

    screen.fill(WHITE)
    draw_polygon(
        screen, BLACK, 11, 150,
        (300 + position_offset[0], 300 + position_offset[1]),
        angle_offset, vertical_scale, horizontal_scale,
        vertical_shear, horizontal_shear,
        flip_vertical, flip_horizontal
    )
    pygame.display.flip()

pygame.quit()