import pygame
pygame.init()

screen = pygame.display.set_mode((1200, 700))  # Размер окна
WHITE = (255, 255, 255)
RED = (255, 0, 0)

done = False
clock = pygame.time.Clock()

circle_start_w = 600
circle_start_h = 350

while not done:
    keys = pygame.key.get_pressed()
    screen.fill(WHITE)  

    if keys[pygame.K_UP] and circle_start_h > 38:
        circle_start_h -= 20
    if keys[pygame.K_DOWN] and circle_start_h < 662:
        circle_start_h += 20
    if keys[pygame.K_LEFT] and circle_start_w > 38:
        circle_start_w -= 20
    if keys[pygame.K_RIGHT] and circle_start_w < 1162:
        circle_start_w += 20

    pygame.draw.circle(screen, RED, (circle_start_w, circle_start_h), 25) 
    pygame.display.flip() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    clock.tick(60) 

pygame.quit()