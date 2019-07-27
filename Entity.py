from pygame.locals import *
import pygame
from Motion import *


class Entity():
    def __init__(self, x: int, y: int, scene_width, scene_height):
        # https://openmoji.org/python3 -m pip install -U pygame --user
        self.terminal_velocity = 8
        self.gravity = self.terminal_velocity / 16

        self.x = Motion(x, 3, -0.1, self.terminal_velocity, scene_width, 0)
        self.y = Motion(y, 3, -0.1, self.terminal_velocity, scene_height, 0)

        self.rot: Motion = Motion(0, 0, 0, 8, 0, 0)

        self.w: float = 64
        self.h: float = 64

        self.dead = False

    def draw(self, screen):
        raise NotImplementedError()

    def update(self, scene_width, scene_height, emoji):
        raise NotImplementedError()

    def update_position(self, scene_width, scene_height):
        #self.constrain_to_screen(scene_width, scene_height)
        self.x.constrain(self.w, 0)
        self.y.constrain(0, self.h)
        self.x.apply_acceleration()
        self.y.apply_acceleration()
        self.y.apply_gravity(scene_height, self.gravity)
        if (self.y.position == scene_height and self.y.velocity == 0):
            self.x.apply_drag(self.gravity / 2)

        self.x.apply_terminal_velocity()
        self.y.apply_terminal_velocity()
        self.x.apply_velocity()
        self.y.apply_velocity()

    def bounce(self):
        self.y.set_motion(-16, 0.01)

    def roll(self, angle):
        pass
