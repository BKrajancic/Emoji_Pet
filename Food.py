import pygame
from Entity import *


class Food(Entity):
    def __init__(self, x: int, y: int, w: int, h: int):
        Entity.__init__(self, x, y, w, h)

        self.files = {
            "croissant": pygame.image.load("openmoji/color/72x72/1F950.png").convert_alpha()
        }

        self.sprite = self.files["croissant"]
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

    def update(self, scene_width, scene_height, emoji, scene_main):
        this_rect = self.get_rect()
        other_rect = emoji.get_rect()

        if (this_rect.colliderect(other_rect) and self.collide):
            #emoji grow by 10%
            emoji.rescale()
            self.dead = True

    def update_position(self, scene_width, scene_height):
        Entity.update_position(self, scene_width, scene_height)

    def yeet(self):
        self.bounce()
        self.x.set_motion(velocity= 10*random.uniform(-1,1), acceleration=0.01)
