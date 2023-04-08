import pygame
import constants as cte
from models import *

pygame.init()

screen = pygame.display.set_mode((cte.SCREEN_X, cte.SCREEN_Y), 0)
text_font = pygame.font.SysFont('arial', 24, True, False)

if __name__ == '__main__':
    pacman = Pacman(cte.SIZE)

    blinky = Enemy(cte.RED, cte.SIZE)
    inky = Enemy(cte.CYAN, cte.SIZE)
    clyde = Enemy(cte.ORANGE, cte.SIZE)
    pinky = Enemy(cte.PINK, cte.SIZE)

    enemies = (blinky, inky, clyde, pinky)

    background = Background(cte.SIZE, text_font, pacman)
    for enemy in enemies:
        background.add_movable(enemy)
    
    # Game loop
    while True:
        # Rules
        pacman.calculate_rules()
        background.calculate_rules()
        for enemy in enemies:
            enemy.calculate_rules()
        
        # Draw
        screen.fill(cte.BLACK)
        background.draw(screen)
        pacman.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        pygame.display.update()
        pygame.time.delay(100)

        # Events
        events = pygame.event.get()
        background.process_events(events)
        pacman.process_events(events)