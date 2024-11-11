import pygame
import random

pygame.init()
size = (800, 800)
BGCOLOR = (255, 255, 255)
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
font = pygame.font.Font("/Users/kevinlacour/Downloads/freedom-font", 30)
done = False
#clock = pygame.time.Clock()


    
def game_loop():
    done = False


class Projectile():

        
 


class Shooter():
    def __init__(self, screen):
        self.image = pygame.draw.circle(screen, GREEN, pos, 20 )
        self.image.fill(255, 0, 0)
        self.alive = True
        self.useWeapons = [Weapon.Gun(), Weapon.Knife()]
        
    def getPos():
        pos = pygame.mouse.get_pos()
        return (pos)
    




    
