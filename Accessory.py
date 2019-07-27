import pygame
from Entity import *


class Accessory(Entity):
    def __init__(self, x: int, y: int, w: int, h: int):
        Entity.__init__(self, x, y, w, h)

        self.files = {
            "cowboy": pygame.image.load("sprites/hat.png").convert_alpha(),
            "sunglasses": pygame.image.load("sprites/sunglasses.png").convert_alpha()
        }

        self.mood = "sunglasses"

        self.sprite = self.files[self.mood]
        self.x.set_motion(velocity=1, acceleration=0.01)
        self.y.set_motion(velocity=1, acceleration=-1)

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
            emoji.mood = self.mood
            self.dead = True
