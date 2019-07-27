from pygame.locals import *
import pygame


class Emoji():
    def __init__(self):
        # https://openmoji.org/python3 -m pip install -U pygame --user
         self.files = {
            "happy": pygame.image.load("sprites/1F60A.png").convert_alpha(),
            "moody": pygame.image.load("sprites/1F62b.png").convert_alpha(),
            "tongue": pygame.image.load("sprites/1F60B.png").convert_alpha(),
            "sad": pygame.image.load("sprites/1F61F.png").convert_alpha()
        }
        self.x: int = 0
        self.y: int = 0
        self.w: int = 64
        self.h: int = 64
        self.vel_x: int = 8
        self.vel_y: int = 8
        self.mood = "happy"
        self.current = self.files[self.mood]

    def draw(self, screen):
        imagerect = self.current.get_rect()
        imagerect.left = self.x
        imagerect.bottom = self.y
        screen.blit(self.current, imagerect)

    def update(self, scene_width, scene_height):

        # if (self.x + self.w > scene_width):
        #    self.vel_x = -abs(self.vel_x)
        # elif (self.x - self.w < 0):
        #    self.vel_x = abs(self.vel_x)

        # if (self.y + self.h > scene_height):
        #    self.vel_y = -abs(self.vel_y)
        # elif (self.y - self.h < 0):
        #    self.vel_y = abs(self.vel_y)

        self.x += self.vel_x
        self.y += self.vel_y
