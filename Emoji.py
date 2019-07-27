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
        self.x: float = 0
        self.y: float = 0
        self.set_motion(vel_x=3, accel_x=-0.3, vel_y=3, accel_y=-1)

        self.w: float = 64
        self.h: float = 64

        self.mood = "happy"
        self.current = self.files[self.mood]
        self.terminal_velocity = 16
        self.gravity = self.terminal_velocity / 16

    def draw(self, screen):
        imagerect = self.current.get_rect()
        imagerect.left = self.x
        imagerect.bottom = self.y
        screen.blit(self.current, imagerect)

    def update(self, scene_width, scene_height):
        self.constrain_to_screen(scene_width, scene_height)
        self.apply_acceleration()

        self.apply_gravity(scene_height, self.gravity)
        self.apply_terminal_velocity(self.terminal_velocity)
        self.apply_velocity()

    def apply_terminal_velocity(self, tv):
        if (self.vel_x < -tv):
            self.vel_x = -tv
        elif (self.vel_x > tv):
            self.vel_x = tv

        if (self.vel_y < -tv):
            self.vel_y = -tv
        elif(self.vel_y > tv):
            self.vel_y = tv

    def constrain_to_screen(self, scene_width, scene_height):
        if (self.x + self.w > scene_width):
            self.vel_x = -abs(self.vel_x)
        elif (self.x < 0):
            self.vel_x = abs(self.vel_x)

        if (self.y > scene_height):
            self.vel_y = -abs(self.vel_y)
        elif (self.y - self.h < 0):
            self.vel_y = abs(self.vel_y)

    def set_motion(self, vel_x, vel_y, accel_x, accel_y):
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.accel_x = accel_x
        self.accel_y = accel_y

    def apply_velocity(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def apply_acceleration(self):
        previous_x = self.vel_x
        previous_y = self.vel_y

        self.vel_x += self.accel_x
        self.vel_y += self.accel_y

        if ((previous_x > 0 and self.vel_x <= 0) or (previous_x < 0 and self.vel_x >= 0)):
            self.accel_x = 0
            self.vel_x = 0

        if ((previous_y > 0 and self.vel_y <= 0) or (previous_y < 0 and self.vel_y >= 0)):
            self.accel_y = 0
            self.vel_y = 0

    def apply_gravity(self, scene_height, gravity):
        if (self.y < scene_height):
            self.accel_y = gravity
