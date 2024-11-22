# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame
import sys

pygame.init()


screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Car and Sun")

RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (135, 206, 250)  
GREEN = (34, 139, 34)  


def draw_scene():

    screen.fill(BLUE)
    
    pygame.draw.rect(screen, GREEN, (0, screen_height - 50, screen_width, 50))
    
    pygame.draw.circle(screen, YELLOW, (500, 80), 50)
    
    pygame.draw.rect(screen, RED, (150, 250, 200, 50))
    pygame.draw.rect(screen, RED, (190, 220, 120, 40))
    
    pygame.draw.rect(screen, BLUE, (200, 230, 40, 30))
    pygame.draw.rect(screen, BLUE, (260, 230, 40, 30))

    pygame.draw.circle(screen, BLACK, (180, 300), 20)
    pygame.draw.circle(screen, BLACK, (320, 300), 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_scene()
    pygame.display.flip()

pygame.quit()
sys.exit()
