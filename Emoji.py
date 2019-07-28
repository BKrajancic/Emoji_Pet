from pygame.locals import *
from Entity import *
import pygame
import math
from Accessory import *


class Emoji(Entity):
    def __init__(self, x: int, y: int, scene_width, scene_height):
        Entity.__init__(self, x, y, scene_width, scene_height)
        # https://openmoji.org/python3 -m pip install -U pygame --user
        self.files = {
            "happy": pygame.image.load("openmoji/color/72x72/1F60A.png").convert_alpha(),
            "moody": pygame.image.load("openmoji/color/72x72/1F62B.png").convert_alpha(),
            "tongue": pygame.image.load("openmoji/color/72x72/1F60B.png").convert_alpha(),
            "sad": pygame.image.load("openmoji/color/72x72/1F61F.png").convert_alpha(),
            "cowboy": pygame.image.load("openmoji/color/72x72/1F920.png").convert_alpha(),
            "sunglasses": pygame.image.load("openmoji/color/72x72/1F60E.png").convert_alpha(),
            "scared": pygame.image.load("openmoji/color/72x72/1F62F.png")
        }

        self.cool_moods = ["cowboy", "sunglasses"]

        self.x.set_motion(5, -0.03)
        self.y.set_motion(3, -1)
        self.mood = "happy"
        self.current = self.files[self.mood]
        self.angle = 0
        self.roll_upright_speed = 8
        self.height = 72
        self.width = 72

    def get_rect(self):
        img = self.current.get_rect(
            right = self.x.position + self.width,
            bottom = self.y.position + self.height,
            left = self.x.position ,
            top = self.y.position)
        #scale_img = pygame.transform.scale(img, (self.height, self.width))
        img_center = img.center
        rot_img = pygame.transform.rotate(self.current, self.angle)
        return rot_img.get_rect(center=img_center)

    def get_img(self):
        surface = self.current
        surface = pygame.transform.scale(surface, (self.height, self.width))
        surface = pygame.transform.rotate(surface, self.angle)
        return surface

    def draw(self, screen):
        screen.blit(self.get_img(), self.get_rect())

    def update(self, scene_width, scene_height):
        self.current = self.files[self.mood]
        self.angle -= self.x.velocity
        self.angle %= 360
        self.roll_upright()
        if (self.mood == "scared" and self.x.velocity == 0 and self.y.velocity == 0):
            self.mood = "happy"

    def roll_upright(self):
        if self.x.velocity == 0 and self.angle != 0:
            self.angle = math.floor(self.angle)
            if (self.angle > 180):
                self.angle += self.roll_upright_speed
            else:
                self.angle -= self.roll_upright_speed

            pre_modulo = self.angle
            self.angle %= 360

            if (pre_modulo != self.angle):
                self.angle = 0

    def rescale(self):
        self.height = int(self.height+10)
        self.width = int(self.width+10)
        #self.y.positon = int(self.y.position+10)

    def roll(self, angle, scene_main):
        self.x.set_motion(angle, 0.05)
        if self.mood in ("cowboy", "sunglasses"):
            scene_main.yeet_accessory()
            self.mood = "scared"

        self.mood = "scared"
