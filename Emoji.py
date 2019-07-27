from pygame.locals import *
from Entity import *
import pygame


class Emoji(Entity):
    def __init__(self, x: int, y: int):
        Entity.__init__(self, x, y)
        # https://openmoji.org/python3 -m pip install -U pygame --user
        self.files = {
            "happy": pygame.image.load("sprites/1F60A.png").convert_alpha(),
            "moody": pygame.image.load("sprites/1F62b.png").convert_alpha(),
            "tongue": pygame.image.load("sprites/1F60B.png").convert_alpha(),
            "sad": pygame.image.load("sprites/1F61F.png").convert_alpha()
        }

        self.set_motion(vel_x=3, accel_x=-0.3, vel_y=3, accel_y=-1)
        self.mood = "happy"
        self.current = self.files[self.mood]

    def draw(self, screen):
        imagerect = self.current.get_rect()
        imagerect.left = self.x
        imagerect.bottom = self.y
        screen.blit(self.current, imagerect)

    def update(self, scene_width, scene_height):
        print("Update")
