from pygame.locals import *
from Entity import *
import pygame
import math
from Accessory import *
from sys import platform

if platform == "linux" or platform == "linux2":
    from grove_rgb_lcd import *


class Emoji(Entity):
    def __init__(self, x: int, y: int, scene_width, scene_height):
        Entity.__init__(self, x, y, scene_width, scene_height)
        # https://openmoji.org/python3 -m pip install -U pygame --user
        self.files = {
            "happy": pygame.image.load("openmoji/color/72x72/1F60A.png").subsurface(10, 10, 50, 50).convert_alpha(),
            "moody": pygame.image.load("openmoji/color/72x72/1F62B.png").subsurface(10, 10, 50, 50).convert_alpha(),
            "tongue": pygame.image.load("openmoji/color/72x72/1F60B.png").subsurface(10, 10, 50, 50).convert_alpha(),
            "sad": pygame.image.load("openmoji/color/72x72/1F61F.png").subsurface(10, 10, 50, 50).convert_alpha(),
            "cowboy": pygame.image.load("openmoji/color/72x72/1F920.png").subsurface(6, 6, 58, 58).convert_alpha(),
            "sunglasses": pygame.image.load("openmoji/color/72x72/1F60E.png").subsurface(10, 10, 54, 54).convert_alpha(),
            "scared": pygame.image.load("openmoji/color/72x72/1F62F.png").subsurface(10, 10, 50, 50).convert_alpha()
        }

        self.cool_moods = ["cowboy", "sunglasses"]

        self.x.set_motion(5, -0.03)
        self.y.set_motion(3, -1)
        self.mood = "happy"
        self.current = self.files[self.mood]
        self.angle = 0
        self.roll_upright_speed = 8
        self.shrink_rate = 0.3
        self.extra_y = 0

    def get_rect(self):
        current = pygame.transform.scale(
            self.current,
            (int(self.h), int(self.w))
        )

        img = current.get_rect(
            left=self.x.position,
            bottom=self.y.position + self.extra_y
        )

        #scale_img = pygame.transform.scale(img, (self.height, self.width))
        img_center = img.center
        rot_img = pygame.transform.rotate(current, self.angle)
        return rot_img.get_rect(center=img_center)

    def get_img(self):
        surface = pygame.transform.scale(
            self.current,
            (int(self.h), int(self.w))
        )

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

        if (self.h > 72):
            self.h = float(self.h) - self.shrink_rate
            #self.extra_y += self.shrink_rate * 0.5

        if (self.h <= 72):
            self.h = 72
            self.extra_y = 0

        if (self.w > 72):
            self.w = float(self.w) - self.shrink_rate

        if (self.w < 72):
            self.w = 72

        if platform == "linux" or platform == "linux2":
            setText(self.mood)
            setRGB(0, 128, 64)

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
        self.h = int(self.h+12)
        self.w = int(self.w+12)
        #self.extra_y += 3.5

    def roll(self, angle, scene_main):
        self.x.set_motion(angle, 0.05)
        if self.mood in ("cowboy", "sunglasses"):
            scene_main.yeet_accessory()
            self.mood = "scared"

        self.mood = "scared"
