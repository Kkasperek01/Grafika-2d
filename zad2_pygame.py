import pygame

pygame.init()


WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prostokąt i trójkąty")


NIEBIESKI = (0, 0, 255)
CZARNY = (0, 0, 0)
BIAŁY = (255, 255, 255)

rect_x, rect_y = 150, 200
rect_width, rect_height = 200, 100


triangle_top = [(rect_x + rect_width // 2, rect_y),
                (rect_x + 40, rect_y - 80),
                (rect_x + rect_width - 40, rect_y - 80)]

triangle_bottom = [(rect_x + rect_width // 2, rect_y + rect_height),
                   (rect_x + 40, rect_y + rect_height + 80),
                   (rect_x + rect_width - 40, rect_y + rect_height + 80)]

running = True
while running:
    win.fill(BIAŁY)


    pygame.draw.rect(win, NIEBIESKI, (rect_x, rect_y, rect_width, rect_height))
    pygame.draw.polygon(win, NIEBIESKI, triangle_top)
    pygame.draw.polygon(win, NIEBIESKI, triangle_bottom)

    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
