import pygame
from Entity import *


class Hat(Entity):
    def __init__(self, x: int, y: int):
        Entity.__init__(self, x, y)
        self.sprite = pygame.image.load(
            "openmoji/color/72x72/1F62b.png").convert_alpha()
        self.set_motion(vel_x=1, accel_x=0.01, vel_y=1, accel_y=-1)

    def draw(self, screen):
        imagerect = self.sprite.get_rect()
        imagerect.left = self.x
        imagerect.bottom = self.y
        screen.blit(self.sprite, imagerect)

    def update(self, scene_width, scene_height):
        print("Update")
