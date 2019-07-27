import pygame
from Entity import *


class Hat(Entity):
    def __init__(self, x: int, y: int, scene_width, scene_height):
        Entity.__init__(self, x, y, scene_width, scene_height)
        self.sprite = pygame.image.load("sprites/hat.png").convert_alpha()
        #pixels = self.sprite.PixelArray(self.sprite)
        #pixels.replace(Color(255, 255, 255, 255), Color(0, 0, 255, 255))
        #self.set_motion(vel_x=1, accel_x=0.01, vel_y=1, accel_y=-1)

    def get_rect(self):
        imagerect = self.sprite.get_rect()
        imagerect.left = self.x.position
        imagerect.bottom = self.y.position
        return imagerect

    def draw(self, screen):
        imagerect = self.get_rect()
        screen.blit(self.sprite, imagerect)

    def update(self, scene_width, scene_height, emoji):
        this_rect = self.get_rect()
        other_rect = emoji.get_rect()
        if (this_rect.colliderect(other_rect)):
            emoji.mood = "cowboy"
            self.dead = True
