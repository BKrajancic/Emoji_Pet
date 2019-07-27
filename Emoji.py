from pygame.locals import *
from Entity import *
import pygame


class Emoji(Entity):
    def __init__(self, x: int, y: int, w: int, h: int):
        Entity.__init__(self, x , y, w, h)
        # https://openmoji.org/python3 -m pip install -U pygame --user
        self.files = {
            "happy": pygame.image.load("openmoji/color/72x72/1F60A.png").convert_alpha(),
            "moody": pygame.image.load("openmoji/color/72x72/1F62B.png").convert_alpha(),
            "tongue": pygame.image.load("openmoji/color/72x72/1F60B.png").convert_alpha(),
            "sad": pygame.image.load("openmoji/color/72x72/1F61F.png").convert_alpha(),
            "cowboy": pygame.image.load("openmoji/color/72x72/1F920.png").convert_alpha(),
            "sunglasses": pygame.image.load("openmoji/color/72x72/1F60E.png").convert_alpha()
        }
        self.set_motion(vel_x=3, accel_x=-0.3, vel_y=3, accel_y=-1)
        self.mood = "happy"
        self.current = self.files[self.mood]

    def get_rect(self):
        imagerect = self.current.get_rect()
        imagerect.left = self.x
        imagerect.bottom = self.y
        return imagerect

    def draw(self, screen):
        imagerect = self.get_rect()
        screen.blit(self.current, imagerect)

    def update(self, scene_width, scene_height):
        self.current = self.files[self.mood]
        pass
